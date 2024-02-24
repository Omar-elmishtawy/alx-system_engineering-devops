# install python package

exec { 'install python package':
  commad => 'pip install flask==2.1.0',
}
