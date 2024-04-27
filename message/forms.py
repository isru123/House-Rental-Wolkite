from django import forms

from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-2 px-4 rounded-lg border',
                'id': 'message-input',
                'style': 'width: 77%; background-color: #F2F2F2; height: 40px;',  # Set initial height here
                'oninput': 'autoResizeTextarea(this)'
            })
        }