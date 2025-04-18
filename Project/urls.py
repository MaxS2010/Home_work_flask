from .settings import project
import home

home.home.add_url_rule(rule= "/", view_func= home.views.render_home)
project.register_blueprint(blueprint=home.app.home)
