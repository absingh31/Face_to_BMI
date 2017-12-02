import json
import pandas as pd

file_list = [
'FD50E18E-FEE1-46BA-BC4C-D83C4D68486A.json',
'50D57451-6184-4E75-B36B-C459CAF603FC.json',
'0AA09892-C260-4BA8-BD5E-7FA0B92596D2.json',
'EF224E7F-2986-44AD-9131-4BE6CFA44B73.json',
'DED11501-1000-41D6-9CB2-C1C8D69CEC58.json',
'0FD71A24-B1F4-48F1-856D-18DC6BEC88F5.json',
'98E247A5-0DAD-4A1E-A612-2781D54C95BF.json',
'DB07A5BD-4B8B-46E1-A0FB-C90580D64F43.json',
'EEB03181-BB33-4931-8A6A-4FFBC62871D5.json',
'1B0DD003-6EAF-4B0D-B446-B07984758309.json',
'928D56DC-5D11-4495-AC6B-5573B33AEE03.json',
'FC863DFE-A41F-4A39-85D8-098EE072604B.json',
'B3D598C4-9976-482E-B0EC-998F43B518AB.json',
'DF7A1891-6EAF-4499-9BBA-9FD53E3E04B6.json',
'A5693743-A522-44A1-8AF1-EDB9B539150D.json',
'046F8922-8FE9-48FF-895C-0228B6AF04A7.json',
'F0D90FBE-F0D2-4EE2-BBBA-1E0883F298E9.json',
'0C0998A5-2D92-4FD7-9F8D-A436C183F557.json',
'489D9CE9-5446-4205-9C88-03ECA9153F74.json',
'E7C06C77-0802-42ED-9BD1-7DCD4DC189E6.json',
'AF8F2B29-FB47-482F-9DDF-95C2383BD995.json',
'690E5C47-AA71-45CB-B26D-73020FB04C56.json',
'EF8E2B2D-F3D6-40EB-8C4D-3CB5D347554B.json',
'FF0B2DC9-3B5A-4246-8953-1FABA6BCCE8E.json',
'41589882-FCD1-4705-9196-EA78694FCEB8.json',
'D6BB31CC-A165-4DF7-BC72-58C291EADB01.json',
'9C1D569D-45CD-4E46-BE2F-7AA028B2FC6D.json',
'FFB83BB2-B58B-48C7-9997-962A7D3BC250.json',
'EF4062A8-8819-41AA-B981-5CE163F886FA.json',
'027B693E-AFDA-470D-9E34-6A888754F078.json',
'12F7CC46-E9A9-4FE8-A356-1DDBB3F032EC.json',
'67CBCC78-BEF8-4A21-9519-2DF0E2D60FAC.json',
'6A3F0EFE-7523-4E5A-B9B9-B894BCBDF625.json',
'9F38E5AB-283A-4AFB-94BC-BF13E3B8CA4B.json',
'64458E24-31BB-4F58-8C4D-3D7CB5F1AD5F.json',
'11199B7E-72DD-4A19-86EB-864FC27955C6.json',
'3ECA2F5D-778E-40B1-9364-D8ED39D0EECE.json',
'BDE3BBB7-2BA1-42A5-B95B-DE998973DD28.json',
'21574B41-AFE7-42EE-8232-937D0591E72B.json',
'8F07F1C9-CE82-4BD1-94E5-FC9D257EEC67.json',
'A0515CF3-F573-423E-A7FC-4336A888E47E.json',
'AA281B12-B71E-49A9-94A3-FD1E20422440.json',
'37E98630-3D54-4941-8640-0CB560FA6102.json',
'A98BF5E7-E56C-41A8-9D95-25A82A144EC2.json',
'E30DF9A0-2124-443E-B996-91D31E130ACD.json',
'783C5FCB-1884-4283-9A53-C2AA49471CB2.json',
'0FE627F3-2D51-4C74-915B-02B77624B160.json',
'C3180DD0-A21A-4372-84B8-915B4E00F26F.json',
'E83878A3-3CFC-42E3-99A3-616193C3BA60.json',
'143DD69D-81AE-4B76-A9F3-5BBCBB8F6870.json',
'510D4432-1779-4458-B00D-AAB852DC7E6F.json',
'A7C0D4BA-3011-4690-A7CB-7B978C4E86BA.json',
'ED59ED4C-004B-4342-9F79-0C2796764362.json',
'DA6884BF-ADEA-4021-BDF7-6D33B062D01A.json',
'C65320A7-6E19-4B3E-8D1E-5A9591EE2864.json',
'7E7CABA5-39BF-42E3-96A4-17A75057E054.json',
'7EB8C457-3D3A-43AE-B953-B268892F28EF.json',
'51D2A651-7C69-4D68-B214-A41BABD18134.json',
'7CF1A043-8C3B-4616-897E-FAEF5468076D.json',
'99D07C28-F0CC-4859-A406-35F17F805BDE.json',
'8BA07A9B-9FBB-4298-A4AC-B543E74BFD6D.json',
'21FD9D6F-6B84-45CA-8434-69940BDF99F4.json',
'47D7F57F-D2AA-4161-9585-D91B74125EE3.json',
'1E703DC2-9051-4084-BD64-51B9DD52F8EB.json',
'B2F52A50-0FE8-46E7-A074-EAFBED6EA56D.json',
'795058EC-5A92-474F-8F0A-94DFA74EE4F7.json',
'AE49BE88-023C-4826-B2DA-226FDD48D480.json',
'52C6420D-F94A-4C00-8197-FC43929916EE.json',
'42BA57F6-F0F0-40B3-8E99-4BC8D1ABF1EA.json',
'333F7D58-F6F7-463A-92F6-41D1E97B2DDA.json',
'F4883F0D-7279-4772-B5C3-B3CBDABEFE3D.json',
'1EDC5863-50F1-492F-A254-063531F4578B.json',
'875956B3-1F57-40E9-91F7-18C64A67A002.json',
'B62A68D0-D5C3-46E2-B19C-0E197901DE98.json',
'C50A7385-4198-4327-BD7D-08C0091E827A.json',
'661C4A2F-0F58-47ED-958D-4210FCEED34A.json',
'754E6542-1167-49DA-85C3-1AB4523A41F9.json',
'6764E148-35E6-4509-8D2F-7F4F365ADB5E.json',
'D289C518-F0BC-44CA-86F3-EAE3E28894EB.json',
'0A23BF41-28BB-4598-958C-C178CEEBFA73.json',
'5284A0B6-B603-4674-A782-F56932031DCF.json',
'DFE53D18-02E1-490A-A68A-FF2FF0B8A943.json',
'923E4A6A-C9BC-4679-968F-498AEACF7DB3.json',
'B90D35CC-9B78-4EAE-A1C6-7E2F0A351FF5.json',
'4110A9CC-E8F6-4E5F-A6E1-1954E5253889.json',
'AD65F415-989C-4AD7-AD5C-6EBA52A83F2C.json',
'5BAC171C-1E48-49B2-BAE6-09BCCAB46129.json',
'0FEDA0A9-7787-4033-9406-2435D3B4C874.json',
'058A9737-3326-47E6-ADC7-A65582860539.json',
'F71FFDB4-EEFC-4000-9E5F-F3101548EB35.json',
'5E735A7F-6CA4-43E6-9F26-6980C3734A28.json',
'1D46240C-F511-4B17-9F25-38DCBE8A5DCA.json',
'CE8A6316-D4E4-4AB1-B2A5-D28595B2DAFB.json',
'49D3351C-5079-42BD-B2E8-83376743AD50.json',
'6F519542-E299-4AFC-B425-0FBC7899C9DF.json',
'E6057E44-568E-4E61-AC7E-7CD7D8C1EC6E.json',
'08CB220B-A129-4075-932C-A05D767CBEBE.json',
'04921E48-9862-4C75-B06B-AA99D8A3ED2E.json',
'EE859ED9-7772-4097-A4E9-086DD29826FD.json',
'3975AE3D-4BD4-4574-8CB1-08678143536B.json',
'011DE72F-C475-4453-B5FC-E7621ABD2EE9.json',
'BC17B8B3-BBC9-4961-A4C6-659D44B6ECC1.json',
'59B5B52F-9F51-4253-AE1F-27C8E2C7B8ED.json',
'67BE28F4-6248-47D1-8381-2EAAB5099400.json',
'5CC993A8-7A3B-42D5-B463-BD9289115129.json',
'C1040660-31B4-486C-9664-700DA51C6A6A.json',
'121891F2-C802-4B5C-B872-38E8AA39F06E.json',
'A682CE6B-D80F-4FED-9BF4-728BCD5E3763.json',
'AD610A9E-639D-459B-8512-1B977A5604B9.json',
'82AA9282-A3F3-473C-8893-747ECAED1D04.json',
'B4B247CE-53F7-45EC-85F3-2BB3D4428F4D.json',
'EFCD9A23-9EFC-4AEB-9271-C9ADDF62917A.json',
'D3DB933C-157F-4852-93A4-CEE6DD4613C8.json'
]

weight_list = []
height_list = []

for json_file in file_list:
    with open('bmiapp-data-2017-04-25\\'+json_file) as json_data:
        d = json.load(json_data)
        weight_list.append(d['weight'])
        height_list.append(d['height'])
    

df = pd.DataFrame(file_list,columns=['file_name'])

df['weight']=weight_list
df['height']=height_list
df.to_csv('height_weight.csv')