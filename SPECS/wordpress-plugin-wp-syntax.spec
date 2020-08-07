%define pluginsdir /usr/share/wordpress/wp-content/plugins

Name:		wordpress-plugin-wp-syntax
Version:	1.0	
Release:	1%{?dist}
Summary:	Syntax highlighting for wordpress.

Group:		Application
License:	GPL
URL:		http://www.connections-pro.com/

Source0:	wp-syntax.%{version}.zip

BuildRequires:	unzip
Requires:	wordpress
BuildArch:      noarch

%description
Syntax highlighting using GeSHi supporting a wide range of popular languages.

%prep
%setup -q -n wp-syntax


%install
%{__install} -d %{buildroot}%pluginsdir/wp-syntax
%{__cp} -ar . %{buildroot}%pluginsdir/wp-syntax/


%files
%defattr(-,root,apache,-)
%pluginsdir/wp-syntax


%changelog
* Wed Jan  3 2018 356878@gmail.com - 1.10-1
- Initial version
