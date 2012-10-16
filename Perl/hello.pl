#!/usr/bin/perl

=pod 

    Hello!
    Estudando: Array, For, If, Print, Sort, Multline Comments

=cut

@nomes = (
    'Alice',
    'Meire',
    'Stephany',
    'Mariana', 
    'Marcos', 
    'Marcio', 
    'Schumman', 
    'Joplin',
    'Daniel',
    'Zuzu',
    'Sofia'
);

foreach $i (sort(@nomes)) {
    if ($i eq('Marcos')) {
        print "Olá, Programmer ($i).\n";
    }
    else {
        print "Olá, $i.\n";
    }
}