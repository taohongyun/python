# coding:utf-8
from flask import Flask,render_template,request,url_for
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from werkzeug.utils import redirect

app = Flask(__name__)

Bootstrap(app)
# bootstrap = Bootstrap(app)
nav=Nav()
nav.register_element('top',Navbar(u'个人网站',
                                    View(u'主页','home'),
                                    View(u'我的简历','about'),
                                    Subgroup(u'学习笔记',
                                             View(u'GIT学习','study_git'),
                                             Separator(),
                                             View(u'项目二', 'service'),
                                    ),
))

nav.init_app(app)
@app.route('/')
def home():
    return render_template('home.html',title_name = 'welcome my homepage!!!')


@app.route('/about')
def about():
    return render_template("resume.html")




@app.route('/study_git')
def study_git():
    return redirect('https://github.com/taohongyun/taohongyun/blob/note/%E3%80%90GIT%E3%80%91%E6%80%BB%E7%BB%93.md')

@app.route('/service')
def service():
    return 'service'

if __name__ == '__main__':
    app.run(debug=True)