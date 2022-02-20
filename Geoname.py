# import uuid
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Geoname:
    geoname_id: str
    name: str
    asciiname: str
    alternatenames: str
    latitude: str
    longitude: str
    feature_class: str
    feature_code: str
    country_code: str
    cc2: str
    admin1_code: str
    admin2_code: str
    admin3_code: str
    admin4_code: str
    population: int
    elevation: str
    dem: str
    timezone: str
    modification_date: str

    def to_json(self) -> Dict[str, Any]:
        return {
            'geoname_id': self.geoname_id,
            'name': self.name,
            'asciiname': self.asciiname,
            'alternatenames': self.alternatenames,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'feature_class': self.feature_class,
            'feature_code': self.feature_code,
            'country_code': self.country_code,
            'cc2': self.cc2,
            'admin1_code': self.admin1_code,
            'admin2_code': self.admin2_code,
            'admin3_code': self.admin3_code,
            'admin4_code': self.admin4_code,
            'population': self.population,
            'elevation': self.elevation,
            'dem': self.dem,
            'timezone': self.timezone,
            'modification_date': self.modification_date,
        }
