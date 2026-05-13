from flask_talisman import Talisman

def enable_talisman(app):

    csp = {
        "default-src": "'self'",
        "frame-ancestors": "'none'",
        "form-action": "'self'"
    }

    Talisman(
        app,
        content_security_policy=csp,
        frame_options="DENY",
        force_https=False
    )