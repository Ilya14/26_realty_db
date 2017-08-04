from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Ads(db.Model):
    __tablename__ = 'ads'

    ad_id = db.Column(db.Integer, index=True, primary_key=True)
    settlement = db.Column(db.String(50))
    under_construction = db.Column(db.Boolean)
    description = db.Column(db.Text)
    price = db.Column(db.Integer, index=True)
    oblast_district = db.Column(db.String(50), index=True)
    living_area = db.Column(db.Float)
    has_balcony = db.Column(db.Boolean)
    address = db.Column(db.String(100))
    construction_year = db.Column(db.Integer, index=True)
    rooms_number = db.Column(db.Integer)
    premise_area = db.Column(db.Float)
    active = db.Column(db.Boolean, index=True)

    def __init__(self,
                 ad_id,
                 settlement,
                 under_construction,
                 description,
                 price,
                 oblast_district,
                 living_area,
                 has_balcony,
                 address,
                 construction_year,
                 rooms_number,
                 premise_area,
                 active):
        self.ad_id = ad_id
        self.settlement = settlement
        self.under_construction = under_construction
        self.description = description
        self.price = price
        self.oblast_district = oblast_district
        self.living_area = living_area
        self.has_balcony = has_balcony
        self.address = address
        self.construction_year = construction_year
        self.rooms_number = rooms_number
        self.premise_area = premise_area
        self.active = active
