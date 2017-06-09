Name:      goto-ups-monitor
Version:   1.0
Release:   1
Url:       https://github.com/warwick-one-metre/gotoupsd
Summary:   Pyro frontend for monitoring the GOTO UPSes via SNMP.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-warwickobservatory, onemetre-obslog-client, net-snmp, %{?systemd_requires}
BuildRequires: systemd-rpm-macros

%description
Part of the observatory software for the Warwick La Palma telescopes.

gotoupsd is a Pyro frontend for monitoring the GOTO UPSes via SNMP.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/gotoupsd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/gotoupsd.service %{buildroot}%{_unitdir}

%pre
%service_add_pre gotoupsd.service

%post
%service_add_post gotoupsd.service

%preun
%stop_on_removal gotoupsd.service
%service_del_preun gotoupsd.service

%postun
%restart_on_update gotoupsd.service
%service_del_postun gotoupsd.service

%files
%defattr(0755,root,root,-)
%{_bindir}/gotoupsd
%defattr(-,root,root,-)
%{_unitdir}/gotoupsd.service

%changelog
