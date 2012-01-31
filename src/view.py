import os
import web

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../templates")

render = web.template.render(template_dir)
