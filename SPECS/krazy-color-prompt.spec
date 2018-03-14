Name:         krazy-color-prompt
Version:      0.0.1
Release:      %(git rev-list --count HEAD)%{?dist}
Summary:      Krazy Color Prompt
Vendor:       Hans Kramer
Group:        HHH
License:      CopyLeft
Prefix:       %_prefix
BuildArch:    noarch

%define git_origin git@github.com:HansKramer/KrazyColorPrompt.git


%description
Krazy Color Prompt

%prep
echo " **********  PREP STAGE   **********"
%{__rm} -rf KrazyColorPrompt
git clone %{git_origin}


%build
echo " **********  BUILD STAGE   **********"


%install
echo " **********  INSTALL STAGE   **********"
%{__mkdir_p} %{buildroot}/%{_libexecdir}/kcp
%{__cp} KrazyColorPrompt/{kcp,kcp_blackbg,kcp_fire,kcp_fire_blue,kcp_gray_bg,kcp_gray_bg_2,kcp_pastel,kcp_row}  %{buildroot}/%{_libexecdir}/kcp/


%clean
echo " **********  CLEAN STAGE   **********"
rm -rf %{buildroot}


%files
%dir %{_libexecdir}/kcp
%{_libexecdir}/kcp/*


%changelog
* Sat Mar 10 2018 Hans Kramer <jlam.kramer@gmail.com>
- Initial package build


