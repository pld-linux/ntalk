Summary:	Talk client for one-on-one Internet chatting.
Summary(de):	Talk-client für 1:1-Internet-Schwätzchen.
Summary(fr):	Client talk pour les conversations à deux sur l'Internet.
Summary(pl):	Klient talk do rozmów jeden-na-jeden w Internecie.
Summary(tr):	Internet üzerinde birebir konuþma - talk - sistemi.
Name:		ntalk
Version:	0.11
Release:	1
Copyright:	BSD
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source:		ftp://sunsite.unc.edu/pub/Linux/system/network/chat/netkit-ntalk-%{version}.tar.gz
Patch0:		netkit-ntalk-misc.patch
Patch1:		netkit-ntalk-install.patch
Patch2:		netkit-ntalk-otalk.patch
Requires:	inetd
BuildRequires:	ncurses-devel
Obsoletes:	talk
Buildroot:	/tmp/%{name}-%{version}-root

%description
This package provides a daemon for the Internet talk protocol,
which allows one-on-one chatting between users on different systems.

%description -l de
Dieses Paket enthält einen Dämon für das Internet-Talk-
Protokoll, das das Chatten von zwei Benutzern auf verschiedenen
Systemen ermöglicht.

%description -l fr
Ce package offre un démon pour le 'Internet Talk Protocol',
qui permet la conversation un-a-un dans la discussion entre les
utilisateurs de différents systèmes.

%description -l pl
Pakiet ten zawiera demona dla internetowego protoko³u talk, 
który umo¿liwia	komunikacjê miêdzy u¿ytkownikami na ró¿nych systemach.

%description -l tr
Bu paket internet talk hizmeti için bir istemci ve sunucu içermektedir. Bu
program 'konuþmak' isteyen kiþilerin terminalinde iki bölüm açacaktýr.
Kullanýcýlardan her biri kendi yazdýklarýný ekranýn alt kýsmýnda, karþý
tarafýn yazdýklarýný ise üst kýsýmda göreceklerdir.

%package client
Summary:        Talk client for one-on-one Internet chatting.
Summary(de):    Talk-client für 1:1-Internet-Schwätzchen.
Summary(fr):    Client talk pour les conversations à deux sur l'Internet.
Summary(pl):    Klient talk do rozmów jeden-na-jeden w Internecie.
Summary(tr):    Internet üzerinde birebir konuþma - talk - sistemi.
Group:          Applications/Networking
Group(pl):      Aplikacje/Sieciowe
Requires:	%{name} = %{version}

%description client
This package provides a client for the Internet talk protocol,
which allows one-on-one chatting between users on different systems.

%description -l de client
Dieses Paket enthält einen Client für das Internet-Talk-
Protokoll, das das Chatten von zwei Benutzern auf verschiedenen
Systemen ermöglicht.

%description -l fr client
Ce package offre un client pour le 'Internet Talk Protocol',
qui permet la conversation un-a-un dans la discussion entre les
utilisateurs de différents systèmes.

%description -l pl client
Pakiet ten zawiera klienta dla internetowego protoko³u talk,
który umo¿liwia komunikacjê miêdzy u¿ytkownikami na ró¿nych systemach.

%description -l tr client
Bu paket internet talk hizmeti için bir istemci ve sunucu içermektedir. Bu
program 'konuþmak' isteyen kiþilerin terminalinde iki bölüm açacaktýr.
Kullanýcýlardan her biri kendi yazdýklarýný ekranýn alt kýsmýnda, karþý
tarafýn yazdýklarýný ise üst kýsýmda göreceklerdir.

%prep
%setup -q -n netkit-ntalk-0.11
%patch0 -p1
%patch1 -p1
export POSIXLY_CORRECT=1
%patch2 -p0
unset POSIXLY_CORRECT

%build

make RPM_OPT_FLAGS="$RPM_OPT_FLAGS -w -I%{_includedir}/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man{1,8}}

make install INSTALLROOT=$RPM_BUILD_ROOT MANDIR=%{_mandir}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[18]/* \
	README BUGS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz BUGS.gz

%attr(711,root,root) %{_sbindir}/*
%{_mandir}/man8/*

%files client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/talk
%{_mandir}/man1/talk.1.gz
