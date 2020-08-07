%define pluginsdir /usr/share/wordpress/wp-content/plugins
%define pluginname wp-piwik

Name:		wordpress-plugin-%pluginname
Version:	1.0.14
Release:	1%{?dist}
Summary:	Adds Piwik stats to your dashboard menu and Piwik code to your wordpress header.

Group:		Application
License:	GPL
URL:		http://wordpress.org/extend/plugins/wp-piwik/

Source0:	%{pluginname}.%{version}.zip

BuildRequires:	unzip
Requires:	wordpress >= 4.0.0
BuildArch:      noarch

%description
Adds Piwik stats to your dashboard menu and Piwik code to your wordpress header.

%prep
%setup -q -n %pluginname


%install
%{__install} -d %{buildroot}%pluginsdir/%pluginname
%{__cp} -ar . %{buildroot}%pluginsdir/%pluginname


%files
%defattr(-,root,apache,-)
%pluginsdir/%pluginname


%changelog
* Fri Jan  5 2018 356878@gmail.com - 1.0.14-1
- Update for version 1.0.14, last version supporting php54

* Wed Jan  3 2018 356878@gmail.com - 1.0.8-1
- Initial version
