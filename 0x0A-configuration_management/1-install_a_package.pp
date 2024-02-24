# Install flask (2.1.0)
exec {'install-flask':
require => Exec['install-python'],
command => '/usr/bin/pip3 install flask==2.1.0'
}

exec {'install-python':
command => '/usr/bin/which python3'
}
