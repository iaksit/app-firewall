
Name: app-firewall-core
Group: ClearOS/Libraries
Version: 5.9.9.2
Release: 2.2%{dist}
Summary: Translation missing (firewall_app_summary) - APIs and install
License: LGPLv3
Packager: ClearFoundation
Vendor: ClearFoundation
Source: app-firewall-%{version}.tar.gz
Buildarch: noarch
Requires: app-base-core
Requires: app-network-core
Requires: firewall
Requires: iptables

%description
Translation missing (firewall_app_long_description)

This package provides the core API and libraries.

%prep
%setup -q -n app-firewall-%{version}
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/firewall
cp -r * %{buildroot}/usr/clearos/apps/firewall/

install -D -m 0755 packaging/firewall-up %{buildroot}/usr/sbin/firewall-up
install -D -m 0755 packaging/firewall.init %{buildroot}/etc/rc.d/init.d/firewall
install -D -m 0755 packaging/firewall.lua %{buildroot}/etc/rc.d/firewall.lua
install -D -m 0755 packaging/rc.firewall %{buildroot}/etc/rc.d/rc.firewall
install -D -m 0755 packaging/rc.firewall.types %{buildroot}/etc/rc.d/rc.firewall.types

%post
logger -p local6.notice -t installer 'app-firewall-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/firewall/deploy/install ] && /usr/clearos/apps/firewall/deploy/install
fi

[ -x /usr/clearos/apps/firewall/deploy/upgrade ] && /usr/clearos/apps/firewall/deploy/upgrade

exit 0

%preun
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-firewall-core - uninstalling'
    [ -x /usr/clearos/apps/firewall/deploy/uninstall ] && /usr/clearos/apps/firewall/deploy/uninstall
fi

exit 0

%files
%defattr(-,root,root)
%exclude /usr/clearos/apps/firewall/packaging
%exclude /usr/clearos/apps/firewall/tests
%dir /usr/clearos/apps/firewall
/usr/clearos/apps/firewall/deploy
/usr/clearos/apps/firewall/language
/usr/clearos/apps/firewall/libraries
/usr/sbin/firewall-up
/etc/rc.d/init.d/firewall
/etc/rc.d/firewall.lua
/etc/rc.d/rc.firewall
/etc/rc.d/rc.firewall.types
