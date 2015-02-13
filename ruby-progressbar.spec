# Generated from progressbar-0.11.0.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	progressbar

Summary:	Ruby/ProgressBar is a text progress bar library for Ruby
Name:		ruby-%{rbname}

Version:	0.21.0
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/peleteiro/progressbar
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems >= 1.3.6
BuildArch:	noarch

%description
Ruby/ProgressBar is a text progress bar library for Ruby. It can indicate
progress with percentage, a progress bar, and estimated remaining time.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
#%dir %{gem_dir}/gems/%{rbname}-%{version}
#%dir %{gem_dir}/gems/%{rbname}-%{version}/lib
%{gem_dir}/gems/%{rbname}-%{version}/lib/*.rb
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{rbname}-%{version}

