Summary:	commons-validator - framework to define validators
Summary(pl):	commons-validator - szkielet do definiowania metod kontroluj±cych poprawno¶æ
Name:		jakarta-commons-validator
Version:	1.2.0
Release:	1
License:	Apache v2.0
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/commons/validator/source/commons-validator-%{version}-src.tar.gz
# Source0-md5:	984074a3707c4a366f0b08db88d41e4d
URL:		http://jakarta.apache.org/commons/validator/
BuildRequires:	ant >= 1.5
BuildRequires:	jakarta-commons-beanutils
BuildRequires:	jakarta-commons-collections
BuildRequires:	jakarta-commons-digester
BuildRequires:	jakarta-commons-logging
BuildRequires:	jakarta-oro
Requires:	jakarta-commons-digester
Requires:	jakarta-oro
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The commons-validator package provides a simple, extendable framework
to define validators (validation methods) and validation rules in an
XML file. There is support for internationalization of validation
rules and error messages.

%description -l pl
Pakiet commons-validator udostêpnia prosty, rozszerzalny szkielet do
definiowania "validatorów" (metod kontroluj±cych poprawno¶æ danych),
oraz regu³ okre¶laj±cych poprawno¶æ w pliku XML. Pakiet obs³uguje
zlokalizowane regu³y poprawno¶ci oraz komunikaty b³êdów.

%prep
%setup -q -n commons-validator-%{version}

%build
ant dist \
	-Dcommons-beanutils.jar=%{_javadir}/commons-beanutils.jar \
	-Dcommons-collections.jar=%{_javadir}/commons-collections.jar \
	-Dcommons-digester.jar=%{_javadir}/commons-digester.jar \
	-Dcommons-logging.jar=%{_javadir}/commons-logging.jar \
	-Doro.jar=%{_javadir}/oro.jar

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install dist/*.jar $RPM_BUILD_ROOT%{_javadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt dist/docs/api
%{_javadir}/*.jar
