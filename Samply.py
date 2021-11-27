# coding:utf-8
from flask import Flask,render_template,request,url_for
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *



app = Flask(__name__)

Bootstrap(app)
# bootstrap = Bootstrap(app)
nav=Nav()
nav.register_element('top',Navbar(u'个人网站',
                                    View(u'主页','home'),
                                    View(u'我的简历','about'),
                                    Subgroup(u'项目',
                                             View(u'项目一','about1'),
                                             Separator(),
                                             View(u'项目二', 'service'),
                                    ),
))

# nav.register_element('top',Navbar(u'安徽联通无线网优-道路评估系统',
# View(u'主页','WirelessLine.test'),
# View(u'关于','WirelessLine.test'),
# Subgroup(u'项目',
# View(u'项目一','WirelessLine.test'),
# Separator(),
# View(u'项目二', 'WirelessLine.test'),
# ),
# ))
nav.init_app(app)
@app.route('/')
def home():
    return render_template('home.html',title_name = 'welcome')


@app.route('/about')
def about():
    return render_template("resume.html")




@app.route('/about1')
def about1():
    return 'about1'

@app.route('/service')
def service():
    return 'service'

if __name__ == '__main__':
    app.run(debug=True)