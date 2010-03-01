%define		plugin	check_asterisk_skype
Summary:	Nagios plugin to check Skype plugin status in Asterisk
Name:		nagios-plugin-%{plugin}
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Networking
Source0:	%{plugin}
Source1:	%{plugin}.cfg
Requires:	nagios-core
Requires:	perl-base >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
This plugin checks for Skype license in Asterisk.

%prep
%setup -qcT
cp -p %{SOURCE0} %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{plugin} $RPM_BUILD_ROOT%{plugindir}/%{plugin}
sed -e 's,@plugindir@,%{plugindir},' %{SOURCE1} > $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
