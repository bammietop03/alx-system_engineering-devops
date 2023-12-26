# puppet_ssh_config.pp

file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/ssh_config',  # Adjust the path if needed, depending on your system
  line   => 'PasswordAuthentication no',
  match  => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  path   => '/home/your_username/.ssh/config',  # Replace with the correct path to your SSH config file
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^#?IdentityFile',
}
