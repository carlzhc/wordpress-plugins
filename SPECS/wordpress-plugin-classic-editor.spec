%define pluginsdir /usr/share/wordpress/wp-content/plugins
%define pluginname classic-editor

Name:		wordpress-plugin-%{pluginname}
Version:	1.5
Release:	1%{?dist}
Summary:	Wordpress classic editor

Group:		Application
License:	GPL
URL:		https://wordpress.org/plugins/classic-editor/

Source0:	%{pluginname}.%{version}.zip

BuildRequires:	unzip
Requires:	wordpress
BuildArch:      noarch

%description
Classic Editor is an official plugin maintained by the WordPress team that
restores the previous ("classic") WordPress editor and the "Edit Post" screen.
It makes it possible to use plugins that extend that screen, add old-style meta
boxes, or otherwise depend on the previous editor.

%prep
%setup -q -n %{pluginname}


%install
%{__install} -d %{buildroot}%pluginsdir/%{pluginname}
%{__cp} -ar . %{buildroot}%pluginsdir/%{pluginname}


%files
%defattr(-,root,apache,-)
%pluginsdir/%{pluginname}


%changelog
* Fri Aug  7 2020 356878@gmail.com - 1.5-1
- Initial version
