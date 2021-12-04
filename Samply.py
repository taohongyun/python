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
                                    Subgroup(u'个人学习',
                                             View(u'git学习','study_git'),
                                             Separator(),
                                             View(u'python基础学习', 'py_one'),
                                             Separator(),
                                             View(u'python进阶学习', 'py_two'),
                                             Separator(),
                                             View(u'markdown学习', 'study_mk'),
                                             Separator(),
                                             View(u'pytest学习', 'study_pytest'),
                                             Separator(),
                                             View(u'软件测试用例学习', 'study_case'),
                                             Separator(),
                                             View(u'缺陷报告学习', 'study_defect'),
                                             Separator(),
                                             View(u'软件测试流程及分类', 'study_test'),


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

@app.route('/py_one')
def py_one():
    return redirect('https://github.com/taohongyun/taohongyun/blob/note/%E3%80%90python%E8%BD%AF%E4%BB%B6%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E3%80%91%E5%AD%A6%E4%B9%A0%E6%80%BB%E7%BB%93.md')

@app.route('/py_two')
def py_two():
    return redirect('https://github.com/taohongyun/taohongyun/blob/note/%E3%80%90python%E8%BD%AF%E4%BB%B6%E8%BF%9B%E9%98%B6%E7%9F%A5%E8%AF%86%E3%80%91%E5%AD%A6%E4%B9%A0%E6%80%BB%E7%BB%93.md')

@app.route('/study_mk')
def study_mk():
    return redirect('https://github.com/taohongyun/taohongyun/blob/note/%E3%80%90MARKDOWN%E3%80%91%E5%9F%BA%E7%A1%80%E6%80%BB%E7%BB%93.md')

@app.route('/study_pytest')
def study_pytest():
    return redirect('https://github.com/taohongyun/taohongyun/blob/note/%E3%80%90pytest%E3%80%91%E5%AD%A6%E4%B9%A0.md')

@app.route('/study_case')
def study_case():
    return redirect('https://github.com/taohongyun/taohongyun/blob/note/%E3%80%90%E6%B5%8B%E8%AF%95%E7%94%A8%E4%BE%8B%E5%AD%A6%E4%B9%A0%E3%80%91%E5%86%85%E5%AE%B9.md')

@app.route('/study_defect')
def study_defect():
    return redirect('https://github.com/taohongyun/taohongyun/blob/note/%E3%80%90%E7%BC%BA%E9%99%B7%E6%8A%A5%E5%91%8A%E3%80%91%E5%AD%A6%E4%B9%A0%E5%86%85%E5%AE%B9.md')

@app.route('/study_test')
def study_test():
    return redirect('https://github.com/taohongyun/taohongyun/blob/note/%E6%B5%8B%E8%AF%95%E4%B8%8E%E5%BC%80%E5%8F%91%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%A8%8B%E5%8F%8A%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%88%86%E7%B1%BB.md')



if __name__ == '__main__':
    app.run(debug=True)