# A puppet manifest installing flask v2.1.0 which is a package from pip3.
package { 'flask':
  ensure   => '2.1.0',
  provider => pip3,
}
