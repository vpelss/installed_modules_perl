#!/usr/bin/perl

use strict;
use ExtUtils::Installed;

my %in;

eval { &main(); };    # Trap any fatal errors so the program hopefully
if ($@) {
    &cgierr("fatal error: $@");
}                     # never produces that nasty 500 server error page.
exit; 

sub main(){
my $inst    = ExtUtils::Installed->new();
my $op;
my @modules = $inst->modules();
 foreach my $module (@modules){
      $op = $op . "<br>" . $module;
}

    print "Content-type: text/html\n";
    print "Cache-Control: max-age=0\n";
    print "Cache-Control: no-store\n";
   print "\n\n";
    #print $output;
    print $op;
};

sub cgierr {

    # --------------------------------------------------------
    # Displays any errors and prints out FORM and ENVIRONMENT
    # information. Useful for debugging.

    #if (my $debug == 0) {
    #    print "Epic fail....";
    #   }
    print "Content-Type: text/html\n\n";
    print "<PRE>\n\nCGI ERROR\n==========================================\n";
    $_[0] and print "Error Message       : $_[0]\n";
    $0    and print "Script Location     : $0\n";
    $]    and print "Perl Version        : $]\n";

    print "\nForm Variables\n-------------------------------------------\n";
    foreach my $key ( sort keys %in ) {
        my $space = " " x ( 20 - length($key) );
        print "$key$space: $in{$key}\n";
    }

    print
      "\nEnvironment Variables\n-------------------------------------------\n";
    foreach my $env ( sort keys %ENV ) {
        my $space = " " x ( 20 - length($env) );
        print "$env$space: $ENV{$env}\n";
    }
    print "\n</PRE>";

    exit -1;
}
