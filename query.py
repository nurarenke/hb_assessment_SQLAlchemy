"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *
from pprint import pprint

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

# The return data type is an instance of the BaseQuery class. If you
# fetch the values for the query, it will return a list.



# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

# An association table manages a many to many relationship. An association
# table creates a cross reference for many tables to reference each other.
# The association table does not have any meaningful fields, it only provides
# fields for other tables to reference.



# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = Brand.query.filter_by(brand_id = 'ram').one()

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = db.session.query(Model).filter(Model.name == 'Corvette', Model.brand_id == 'che').all()

# Get all models that are older than 1960.
q3 = db.session.query(Model).filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
q4 = db.session.query(Brand).filter(Brand.founded > 1920).all()

# Get all models with names that begin with ``Cor``.
q5 = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = db.session.query(Brand).filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = db.session.query(Brand).filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

# Get all models whose brand_id is not ``for``.
q8 = db.session.query(Model).filter(Model.brand_id != 'for').all()



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    # Query that returns a list of tuples of model info for a particular year
    model_info = db.session.query(Model.name, Brand.name, Brand.headquarters).join(
        Brand).filter(Model.year == year).all()

    # Unpack each item in the tuple to print and format 
    for model_name, brand_name, brand_headquarters in model_info:
        print 'Model Name:{} | Brand Name:{} | Brand Headquarters:{} \n'.format(
            model_name, brand_name, brand_headquarters)

def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    # Query that returns a list of tuples each brand and it's model info
    total_brands = db.session.query(Brand.name, Model.name, Model.year).join(
        Model).order_by(Brand.name).all()

    current_brand_name = ''

    # unpack each item in the tuple
    for brand_name, model_name, model_year in total_brands:
        # if the brand_name is not already the current brand_name at the top
        if current_brand_name != brand_name:
            # store the current brand_name and then print it
            current_brand_name = brand_name
            print "\n" + brand_name
        # otherwise if current_brand_name does equal the brand_name just print
        # the other necessary info underneath it 
        print '{} {}'.format(model_name, model_year)
    


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    pass


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    pass

