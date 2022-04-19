# File that you can connect to a server without typing a password.
exec { 'echo':
  path    => '/bin/',
  command => 'echo "IdentityFile ~/.ssh/school\n PasswordAuthentication no" >> /etc/ssh/ssh_config',
}
