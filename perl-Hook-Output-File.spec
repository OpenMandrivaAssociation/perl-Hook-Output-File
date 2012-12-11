%define upstream_name    Hook-Output-File
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Redirect STDOUT/STDERR to a file
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Hook/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(boolean)
BuildRequires:	perl(Carp)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::Capture)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Tie::Handle)
BuildArch:	noarch

%description
'Hook::Output::File' redirects 'STDOUT/STDERR' to a file.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Fri Jun 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 682658
- update to new version 0.07

* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.60.0-2
+ Revision: 655028
- rebuild for updated spec-helper

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 401655
- rebuild using %%perl_convert_version
- fixed license field

* Wed Mar 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2009.1
+ Revision: 348536
- update to new version 0.06

* Wed Feb 18 2009 Jérôme Quelin <jquelin@mandriva.org> 0.05-1mdv2009.1
+ Revision: 342374
- update to new version 0.05

* Tue Jan 20 2009 Jérôme Quelin <jquelin@mandriva.org> 0.04-1mdv2009.1
+ Revision: 331591
- import perl-Hook-Output-File


* Tue Jan 20 2009 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist

