#!/usr/bin/perl -w
# TEST.pl: evaluate language guesser
# usage: TEST.pl
# 20130208 erikt(at)xs4all.nl

use strict;

my $command = $0;
my $DUTCHFILE = "$command.dutch.$$";
my $OTHERFILE = "$command.other.$$";
my $maxBuffer = 100; # stop reading test data when buffer reaches this size
my $MINIMUM = 3004; # number of lines used for training

# read test data
my $TESTFILE = "TEST";
my @buffer = ();
my $dutch = 0;
my $other = 0;
my $counter = 0;
if (not open(INFILE,$TESTFILE)) { die "$command: cannot read $TESTFILE\n"; }
if (not open(DUTCHFILE,">$DUTCHFILE")) { die "$command: cannot write $DUTCHFILE\n"; }
if (not open(OTHERFILE,">$OTHERFILE")) { die "$command: cannot write $OTHERFILE\n"; }
while (<INFILE>) {
   my $line = $_;
   chomp($line);
   $counter++;
   if ($counter <= $MINIMUM) { next; }
   if ($line !~ /^(\S)\s(.*)$/) { die "$command: unexpected line: $line\n"; }
   my ($class,$tweet) = ($1,$2);
   if ($class eq ".") { push(@buffer,$tweet); }
   else {
      print DUTCHFILE "$tweet\n";
      $dutch++;
      foreach my $other (@buffer) { print OTHERFILE "$other\n"; }
      $other += $#buffer+1;
      @buffer = ();
   }
   # test file is only partially annotated
   # stop when we see no more positive annotations
   if ($#buffer+1 >= $maxBuffer) { last; }
}
close(OTHERFILE);
close(DUTCHFILE);
close(INFILE);

my $guessLanguage = "tr '[:upper:]' '[:lower:]' | sed 's/http[^ ]*//g'| tokenize | /home/cloud/software/LanguageIdentification/run";
my $dutchCorrect = 0;
my $dutchWrong = 0;
if (not open(INFILE,"cat $DUTCHFILE | $guessLanguage |")) { die "$command: cannot process $DUTCHFILE\n"; }
while (<INFILE>) {
   my $line = $_;
   chomp($line);
   $line =~ s/\s(.*)//;
   my $tweet = $1;
   my $lang = $line;
   if ($lang eq "dutch") { $dutchCorrect++; }
   else {
      $dutchWrong++; 
      if (defined $ARGV[0]) { print "$lang $tweet\n"; }
   }
}
close(INFILE);

my $otherCorrect = 0;
my $otherWrong = 0;
if (not open(INFILE,"cat $OTHERFILE | $guessLanguage |")) { die "$command: cannot process $OTHERFILE\n"; }
while (<INFILE>) {
   my $line = $_;
   chomp($line);
   $line =~ s/\s(.*)//;
   my $tweet = $1;
   my $lang = $line;
   if ($lang ne "dutch") { $otherCorrect++; }
   else { 
      $otherWrong++; 
      if (defined $ARGV[0]) { print "$lang $tweet\n"; }
   }
}
close(INFILE);

my $precision = 100*$dutchCorrect/($dutchCorrect+$otherWrong);
my $recall = 100*$dutchCorrect/($dutchCorrect+$dutchWrong);
printf "used: %d tweets; dutch: %d; other: %d\n",$dutch+$other,$dutch,$other;
printf "precision: %d%%; recall: %d%%\n",$precision,$recall;
print "(all scores: $dutchCorrect $dutchWrong $otherCorrect $otherWrong)\n";

unlink($DUTCHFILE);
unlink($OTHERFILE);

exit(0);
