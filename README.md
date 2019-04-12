# heroku-flask-helloworld

## Requirements

Install heroku command line interface and git

https://devcenter.heroku.com/articles/getting-started-with-python#set-up


## QuickStart

Login

```
$ heroku login
```

```
$ git clone https://github.com/xiaopeng163/heroku-flask-helloworld
$ cd heroku-flask-helloworld
$ heroku create --buildpack heroku/python
Creating app... done, ⬢ young-meadow-44665
Setting buildpack to heroku/python... done
https://young-meadow-44665.herokuapp.com/ | https://git.heroku.com/young-meadow-44665.git
```

PUSH

```
git push heroku master
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 12 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (10/10), 5.73 KiB | 5.73 MiB/s, done.
Total 10 (delta 1), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Python app detected
remote: -----> Installing python-3.6.8
remote: -----> Installing pip
remote: -----> Installing SQLite3
remote: -----> Installing requirements with pip
remote:        Collecting Click==7.0 (from -r /tmp/build_052145e774c4485f7ff1792220c6736f/requirements.txt (line 1))
remote:          Downloading https://files.pythonhosted.org/packages/fa/37/45185cb5abbc30d7257104c434fe0b07e5a195a6847506c074527aa599ec/Click-7.0-py2.py3-none-any.whl (81kB)
remote:        Collecting Flask==1.0.2 (from -r /tmp/build_052145e774c4485f7ff1792220c6736f/requirements.txt (line 2))
remote:          Downloading https://files.pythonhosted.org/packages/7f/e7/08578774ed4536d3242b14dacb4696386634607af824ea997202cd0edb4b/Flask-1.0.2-py2.py3-none-any.whl (91kB)
remote:        Collecting gunicorn==19.9.0 (from -r /tmp/build_052145e774c4485f7ff1792220c6736f/requirements.txt (line 3))
remote:          Downloading https://files.pythonhosted.org/packages/8c/da/b8dd8deb741bff556db53902d4706774c8e1e67265f69528c14c003644e6/gunicorn-19.9.0-py2.py3-none-any.whl (112kB)
remote:        Collecting itsdangerous==1.1.0 (from -r /tmp/build_052145e774c4485f7ff1792220c6736f/requirements.txt (line 4))
remote:          Downloading https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl
remote:        Collecting Jinja2==2.10.1 (from -r /tmp/build_052145e774c4485f7ff1792220c6736f/requirements.txt (line 5))
remote:          Downloading https://files.pythonhosted.org/packages/1d/e7/fd8b501e7a6dfe492a433deb7b9d833d39ca74916fa8bc63dd1a4947a671/Jinja2-2.10.1-py2.py3-none-any.whl (124kB)
remote:        Collecting MarkupSafe==1.1.1 (from -r /tmp/build_052145e774c4485f7ff1792220c6736f/requirements.txt (line 6))
remote:          Downloading https://files.pythonhosted.org/packages/b2/5f/23e0023be6bb885d00ffbefad2942bc51a620328ee910f64abe5a8d18dd1/MarkupSafe-1.1.1-cp36-cp36m-manylinux1_x86_64.whl
remote:        Collecting Werkzeug==0.15.2 (from -r /tmp/build_052145e774c4485f7ff1792220c6736f/requirements.txt (line 7))
remote:          Downloading https://files.pythonhosted.org/packages/18/79/84f02539cc181cdbf5ff5a41b9f52cae870b6f632767e43ba6ac70132e92/Werkzeug-0.15.2-py2.py3-none-any.whl (328kB)
remote:        Installing collected packages: Click, Werkzeug, MarkupSafe, Jinja2, itsdangerous, Flask, gunicorn
remote:        Successfully installed Click-7.0 Flask-1.0.2 Jinja2-2.10.1 MarkupSafe-1.1.1 Werkzeug-0.15.2 gunicorn-19.9.0 itsdangerous-1.1.0
remote:
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote:
remote: -----> Compressing...
remote:        Done: 45.1M
remote: -----> Launching...
remote:        Released v3
remote:        https://young-meadow-44665.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/young-meadow-44665.git
 * [new branch]      master -> master
```
