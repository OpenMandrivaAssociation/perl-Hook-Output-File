
%define realname   Hook-Output-File
%define version    0.05
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Redirect STDOUT/STDERR to a file
Source:     http://www.cpan.org/modules/by-module/Hook/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Carp)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(IO::Capture)
BuildRequires: perl(Test::More)
BuildRequires: perl(Tie::Handle)
BuildRequires: perl(Module::Build::Compat)

BuildArch: noarch

%description
'Hook::Output::File' redirects 'STDOUT/STDERR' to a file.





%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


