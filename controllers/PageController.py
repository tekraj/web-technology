import os
import re
from flask import flash
from werkzeug.utils import secure_filename
from models.db import db
from models.Page import Page
from models.PageImage import PageImage

class PageController:
    UPLOAD_FOLDER = 'static/uploads/'

    @staticmethod
    def list_pages(page_number=1, per_page=10):
        try:
            pages = Page.query.paginate(page=page_number, per_page=per_page)
            return pages
        except Exception as e:
            print(e)
            return []
        
    @staticmethod
    def create_page(name, description,images=None):
        try:
            url = re.sub(r'\W+', '-', name.lower().strip())
            new_page = Page(name=name, url=url, description=description)
            db.session.add(new_page)
            db.session.commit()
            #upload images 
            if images:
                PageController.add_images_to_page(new_page.id,images)
            return new_page
        except Exception as e:
            print(e)
            db.session.rollback()
            flash("Invalid Data", "error")
            raise False
    
    @staticmethod
    def get_page_by_id(page_id):
        page = Page.query.get(page_id)
        page_images = PageImage.query.filter(PageImage.page_id==page.id).all()
        return (page,page_images)
    
    @staticmethod
    def update_page(page_id, name=None,  description=None,images=None):
        page,page_images = PageController.get_page_by_id(page_id)
        if not page:
            return None
        try:
            if name:
                page.name = name
                url = re.sub(r'\W+', '-', name.lower().strip())
            if description:
                page.description = description
            db.session.commit()
            if images:
                PageController.add_images_to_page(page.id,images)
            return page
        except Exception as e:
            db.session.rollback()
            raise e
    
    @staticmethod
    def delete_page(page_id):
        page = PageController.get_page_by_id(page_id)
        if not page:
            return False
        try:
            db.session.delete(page)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def add_images_to_page(page_id, images):
        try:
            for image in images:
                filename = secure_filename(image.filename)
                filepath = os.path.join(PageController.UPLOAD_FOLDER, filename)
                image.save(filepath)
                new_image = PageImage(image=filename, page_id=page_id)
                db.session.add(new_image)
            
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
    def get_page_by_url(url):
        print(url)
        page = Page.query.filter(Page.url==url).first()
        if(page==None):
            return (None,[])
        page_images = PageImage.query.filter(PageImage.page_id==page.id).all()
        return (page,page_images)