# install python package

exec { 'install python package':
  command => '/usr/bin/pip3 install flask==2.1.0',
}
