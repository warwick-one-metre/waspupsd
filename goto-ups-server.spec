Name:      goto-ups-server
Version:   2.0
Release:   0
Url:       https://github.com/warwick-one-metre/gotoupsd
Summary:   Pyro frontend for monitoring the GOTO UPSes via SNMP.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
%if 0%{?suse_version}
Requires:  python3, python34-Pyro4, python34-warwick-observatory-common, python34-warwick-w1m-power, observatory-log-client, net-snmp, %{?systemd_requires}
BuildRequires: systemd-rpm-macros
%endif
%if 0%{?centos_ver}
Requires:  python34, python34-Pyro4, python34-warwick-observatory-common, python34-warwick-w1m-power, observatory-log-client, net-snmp, %{?systemd_requires}
%endif

%description
Part of the observatory software for the Warwick La Palma telescopes.

gotoupsd is a Pyro frontend for monitoring the GOTO UPSes via SNMP.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/gotoupsd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/gotoupsd.service %{buildroot}%{_unitdir}


%pre
%if 0%{?suse_version}
%service_add_pre gotoupsd.service
%endif

%post
%if 0%{?suse_version}
%service_add_post gotoupsd.service
%endif
%if 0%{?centos_ver}
%systemd_post gotoupsd.service
%endif

%preun
%if 0%{?suse_version}
%stop_on_removal gotoupsd.service
%service_del_preun gotoupsd.service
%endif
%if 0%{?centos_ver}
%systemd_preun gotoupsd.service
%endif

%postun
%if 0%{?suse_version}
%restart_on_update gotoupsd.service
%service_del_postun gotoupsd.service
%endif
%if 0%{?centos_ver}
%systemd_postun_with_restart gotoupsd.service
%endif

%files
%defattr(0755,root,root,-)
%{_bindir}/gotoupsd
%defattr(-,root,root,-)
%{_unitdir}/gotoupsd.service

%changelog
