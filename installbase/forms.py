from django import forms
from .models import installbase
from bootstrap_datepicker_plus import DatePickerInput

class InstallBaseform(forms.ModelForm):
    class Meta:
        model = installbase
        fields = ['production', 'customer', 'installedat', 'project_name', 'model', 'osversion', 'serialnumber', 'hostname', 'licensed', 'ipslist', 'shelfmodel', 'disk', 'diskmodel', 'shelfemptyslot', 'slotinfo', 'installedate', 'warrantydate', 'engineername', 'controllereoa', 'controllereos', 'sanswitch', 'sanswitchserial', 'sanswitchmodel', 'sanswitchhostname', 'sanswitchport', 'sanswitchportlicense', 'sanswitchipaddress', 'addlist']
        widgets = {
            'licensed': forms.CheckboxSelectMultiple(),
            'production': forms.RadioSelect(choices=((True, '운영'), (False, '백업'))),
            'customer': forms.TextInput(attrs={'class': 'form-control'}),
            'installedat': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'osversion': forms.TextInput(attrs={'class': 'form-control'}),
            'serialnumber': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'hostname': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'ipslist': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
            'shelfmodel': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'disk': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'diskmodel': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'shelfemptyslot': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'slotinfo': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'sanswitch': forms.Select(choices=((False, '없음'), (True, '있음'))),
            'sanswitchserial': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'disabled': True}),
            'sanswitchmodel': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'disabled': True}),
            'sanswitchhostname': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'disabled': True}),
            'sanswitchport': forms.TextInput(attrs={'class': 'form-control', 'disabled': True}),
            'sanswitchportlicense': forms.TextInput(attrs={'class': 'form-control', 'disabled': True}),
            'sanswitchipaddress': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'disabled': True}),
            'engineername': forms.TextInput(attrs={'class': 'form-control'}),
            'addlist': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'installedate': DatePickerInput(format='%m/%d/%Y'),
            'warrantydate': DatePickerInput(format='%m/%d/%Y'),
            'controllereoa': DatePickerInput(format='%m/%d/%Y'),
            'controllereos': DatePickerInput(format='%m/%d/%Y'),

        }
        labels = {
            'production': '운영/백업',
            'customer': '고객사',
            'installedat': '설치 위치',
            'project_name': '프로젝트명',
            'model': '스토리지 모델',
            'osversion': 'OS버전',
            'serialnumber': '시리얼',
            'hostname': 'HOSTNAME',
            'ipslist': 'IP 리스트',
            'shelfmodel': 'Shelf 모델',
            'disk': 'Disk 수량',
            'diskmodel': 'Disk 모델',
            'shelfemptyslot': 'Shelf 빈슬롯 정보',
            'slotinfo': '컨트롤러 슬롯 정보',
            'engineername': '담당 엔지니어',
            'addlist': '증설 이력',
            'installedate': '초기설치일',
            'warrantydate': '워런티 종료일',
            'controllereoa': '컨트롤러 EOA',
            'controllereos': '컨트롤러 EOS',
            'sanswitch': 'SAN Switch',
            'sanswitchserial': 'SAN Switch Serial',
            'sanswitchmodel': 'SAN Switch Model',
            'sanswitchhostname': 'SAN Switch HostName',
            'sanswitchport': 'SAN Switch 잔여 포트',
            'sanswitchportlicense': 'SAN Switch 포트 라이센스 수량',
            'sanswitchipaddress': 'SAN Switch IP Address',
        }
