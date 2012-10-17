#!/usr/bin/perl

=pod

    Exercício: Somar em pares de números os valores do array @valores;
    Arrays, Subroutines, Strings, For e Ternary operator.

=cut


sub soma {
    print  "$_[0] + $_[1] = ", $_[0] + $_[1], "\n";
}

sub executarSoma {
    @valores = (
        2, 7,
        2, 5,
        10, 12,
        120, 23,
        12, 34
    );

    for ($i = 0; $i < scalar(@valores); $i += 1) {
        $i % 2 == 0 ? push(@indexPares, $valores[$i]) : push(@indexImpares, $valores[$i]);
    }

    for ($i = 0; $i < scalar(@indexPares); $i += 1) {
        print $i + 1, ") ";
        soma($indexPares[$i], $indexImpares[$i]);
    }
}
executarSoma();