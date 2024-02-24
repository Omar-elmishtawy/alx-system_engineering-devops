#kill process
exec { 'Kill prorcess':
  command => '/usr/bin/pkill killmenow',
}
