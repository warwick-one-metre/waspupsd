Name:      wasp-ups-server
Version:   2.2.1
Release:   0
Url:       https://github.com/warwick-one-metre/waspupsd
Summary:   Pyro frontend for monitoring the SuperWASP UPSes via SNMP.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-warwick-observatory-common, python3-warwick-observatory-power
Requires:  observatory-log-client, net-snmp-utils, %{?systemd_requires}

%description
Part of the observatory software for the Warwick La Palma telescopes.

waspupsd is a Pyro frontend for monitoring the SuperWASP UPSes via SNMP.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/waspupsd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/waspupsd.service %{buildroot}%{_unitdir}

%post
%systemd_post waspupsd.service

%preun
%systemd_preun waspupsd.service

%postun
%systemd_postun_with_restart waspupsd.service

%files
%defattr(0755,root,root,-)
%{_bindir}/waspupsd
%defattr(-,root,root,-)
%{_unitdir}/waspupsd.service

%changelog
