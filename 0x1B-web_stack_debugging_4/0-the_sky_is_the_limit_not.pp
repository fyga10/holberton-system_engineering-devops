# Fixes problem of high amount of requests
exec { 'change_limit':
  command  => 'sed -i "s/15/4069/g" /etc/default/nginx; sudo service nginx restart',
  provider => shell,
}
