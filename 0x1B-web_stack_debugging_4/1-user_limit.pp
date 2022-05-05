# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.
exec { 'soft' :
  command  => 'sed -i s/4/4069/ /etc/security/limits.conf',
  provider => shell,
}
exec { 'hard' :
  command  => 'sed -i s/5/4069/ /etc/security/limits.conf',
  provider => shell,
}
