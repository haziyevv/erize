import streamlit as st
from io import BytesIO

def generate_letter(name, phone, email, towhom):
    letter = f"""
Hörmətli "{towhom}" Rəhbərliyi,

Mən, {name}, Ağ şəhər Toca Residence, 40 ünvanında yaşayan bir sakinəm. Son dövrlərdə binamızda qaz təchizatı ilə bağlı ciddi problemlər yaşanır. Qazın tez-tez kəsilməsi və qeyri-sabit verilməsi sakinlər üçün ciddi çətinliklər yaradır. Bu problem təkcə məişət şəraitimizi çətinləşdirmir, eyni zamanda təhlükəsizlik baxımından da ciddi narahatlıq doğurur. Kombinin sönməsi bir yana, əsas məsələ odur ki, qaz təchizatındakı qeyri-sabitlik potensial təhlükə yaradır. Qaz sızması və ya digər fövqəladə halların baş verməsi halında bunun məsuliyyətini kim daşıyacaq?

Bu məsələ ilə bağlı aidiyyəti qurumlara dəfələrlə müraciət etmişik. Mütəxəssislər gəlib müəyyən baxış keçiriblər, lakin problem tam həll olunmamış qalır.

Sizdən xahiş edirik ki, bu məsələyə diqqət yetirəsiniz və problemin köklü həll olunması üçün aidiyyəti qurumlarla əməkdaşlıq edərək lazımi tədbirlər görəsiniz. Məsələnin həlli ilə bağlı hər hansı bir addım atılarsa və ya əlavə məlumat tələb olunarsa, bizimlə əlaqə saxlamağınızı xahiş edirik.

Əlaqə məlumatlarım:
📞 Telefon: {phone}
📧 E-poçt: {email}

Ümid edirik ki, məsələ ən qısa zamanda həll olunacaq.

Hörmətlə,
{name}
"""
    return letter

def get_text_file(letter):
    output = BytesIO()
    output.write(letter.encode())
    output.seek(0)
    return output

# Streamlit app
st.title("Şikayət Məktubu Generatoru")
st.write("Ad, telefon nömrənizi və emailinizi daxil edin, avtomatik olaraq məktub yaradılacaq və endirilmək üçün təqdim olunacaq.")

name = st.text_input("Adınız Soyadınız")
phone = st.text_input("Telefon nömrəniz")
email = st.text_input("E-poçt ünvanınız")
towhom = st.selectbox("Göndəriləcək qurum", ['Bakı Ağ Şəhər', 'Azəriqaz'])

if st.button("Məktubu Yarat və Endir"):
    letter = generate_letter(name, phone, email, towhom)
    st.text_area("Yaradılmış Məktub", letter, height=300)
    
    text_file = get_text_file(letter)
    st.download_button(
        label="Məktubu Endir",
        data=text_file,
        file_name="shikayet_mektubu.txt",
        mime="text/plain"
    )
