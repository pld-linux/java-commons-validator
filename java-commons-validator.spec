Summary:	commons-validator - framework to define validators
Summary(pl):	commons-validator - szkielet do definiowania metod kontrolujących poprawność
Name:		jakarta-commons-validator
Version:	1.0.2
Release:	0.1
License:	Apache License
Source0:	http://www.apache.org/dist/jakarta/commons/validator/source/commons-validator-%{version}-src.tar.gz
# Source0-md5:	917cf3d82847e497e11f9e86488d4b56
Group:		Development/Languages/Java
URL:		http://jakarta.apache.org/commons/validator/
BuildRequires:	jakarta-ant >= 1.5
BuildRequires:	jakarta-oro
Requires:	jakarta-oro
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
The commons-validator package provides a simple, extendable framework
to define validators (validation methods) and validation rules in an
XML file. There is support for internationalization of validation
rules and error messages.

%description -l pl
Pakiet commons-validator udostępnia prosty, rozszerzalny szkielet do
definiowania "validatorów" (metod kontrolujących poprawność danych),
oraz reguł określających poprawność w pliku XML. Pakiet obsługuje
zlokalizowane reguły poprawności oraz komunikaty błędów.

%prep
%setup -q -n commons-validator-%{version}-src

%build
ant \
    -Doro.jar=%{_javalibdir}/oro.jar \
    dist

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
cp dist/*.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dist/docs/api dist/LICENSE.txt
%{_javalibdir}/*.jar
