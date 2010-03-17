%define version	0.9
%define release	%mkrel 5

Name:		ruby-progressbar
Summary:	A Text Progress Bar Library for Ruby
Version:	%{version}
Release:	%{release}
Group:		Development/Ruby
License:	GPL
URL:		http://namazu.org/~satoru/ruby-progressbar/
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:	ruby
BuildRequires:	ruby
BuildArch:	noarch

%description
A Text Progress Bar Library for Ruby.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}%{ruby_sitelibdir}
cp progressbar.rb ${RPM_BUILD_ROOT}%{ruby_sitelibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%check
ruby test.rb

%files
%defattr(-,root,root)
%doc ChangeLog progressbar.en.rd progressbar.ja.rd test.rb
%{ruby_sitelibdir}/*

