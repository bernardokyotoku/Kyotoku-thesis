#pragma rtGlobals=1		// Use modern global access method.
Structure tri
	double r
	double g
	double b
EndStructure

Function plot()
Variable i
String w
Variable/G r,g,b
Display
for(i=1;i<101;i+=1)
	sprintf w,"wave%d",i
	hsv2rgb(300-(i-2)*300/100,1,0.8)
	AppendToGraph $w vs wave0
	ModifyGraph  rgb($w)=(r,g,b)
	
endfor
SetAxis left -40,-15
ModifyGraph nticks(bottom)=10
Label bottom "\\F'Arial'\Z18Wavelength (nm)"
Label left "\\F'Arial'\Z18Transmission (dB)"
ModifyGraph fSize(bottom)=18
ModifyGraph font(bottom)="Arial"
ModifyGraph fSize(left)=18
ModifyGraph font(left)="Arial"
ModifyGraph lblMargin(left)=1
ModifyGraph margin(bottom)=60
ModifyGraph lblMargin(bottom)=1
ModifyGraph width={Aspect,3}
ModifyGraph height=250
DoWindow/C plotImage
ModifyGraph mirror=1
ModifyGraph tick=2
TextBox/C/N=text1/F=0/A=MC "\\JC\\F'Arial'\\Z12Waveguide\r2"
TextBox/C/N=text1/F=0/A=MC "\\JC\\F'Arial'\\Z12Waveguide\r3"
TextBox/C/N=text1/F=0/A=MC "\\JC\\F'Arial'\\Z12Waveguide\r4"

End
/////////////////////////////
Function plot2()
Variable i
String w
Variable/G r,g,b
Display
for(i=1;i<101;i+=10)
	sprintf w,"wave%d",i
	hsv2rgb(300-(i-2)*300/100,1,0.8)
	AppendToGraph $w vs wave0
	ModifyGraph  rgb($w)=(r,g,b)
	
endfor
SetAxis left -40,-15
SetAxis bottom 1483,1495
ModifyGraph nticks(bottom)=10
Label bottom "\\F'Arial'\Z18Wavelength (nm)"
Label left "\\F'Arial'\Z18Transmission (dB)"
ModifyGraph fSize(bottom)=18
ModifyGraph font(bottom)="Arial"
ModifyGraph fSize(left)=18
ModifyGraph font(left)="Arial"
ModifyGraph lblMargin(left)=1
//ModifyGraph margin(bottom)=60
ModifyGraph lblMargin(bottom)=1
ModifyGraph width={Aspect,1.6}
ModifyGraph height=200
DoWindow/C plotChannels
ModifyGraph tick(bottom)=2,mirror=1
ModifyGraph tick(left)=2
ModifyGraph manTick(bottom)={1,2,0,0},manMinor(bottom)={0,50}
Legend/C/N=text0/J/A=MC "\F'Arial'\Z12\JCOutput\rchannel\r\JL\\s(wave1) ch 1\r\\s(wave11) ch 2\r\\s(wave21) ch 3\r\\s(wave31) ch 4\r\\s(wave41) ch 5\r\\s(wave51) ch 6\r\\s(wave61) ch 7";DelayUpdate
AppendText "\\s(wave71) ch 8\r\\s(wave81) ch 9\r\\s(wave91) ch10"
TextBox/C/N=text1/F=0/A=LT/X=0.00/Y=0.00/E=2 "\\Z20\\F'Arial'b)"

End

/////////////////////////////////////////////
Function plot3()
Variable i
String w
Variable/G r,g,b
Display
for(i=1;i<101;i+=1)
	sprintf w,"wave%d",i
	hsv2rgb(300-(i-2)*300/100,1,0.8)
	AppendToGraph $w vs wave0
	ModifyGraph  rgb($w)=(r,g,b)
	
endfor
SetAxis left -40,-15
ModifyGraph nticks(bottom)=3
Label bottom "\\F'Arial'\Z18Wavelength (nm)"
Label left "\\F'Arial'\Z18Transmission (dB)"
ModifyGraph fSize(bottom)=18
ModifyGraph font(bottom)="Arial"
ModifyGraph fSize(left)=18
ModifyGraph font(left)="Arial"
ModifyGraph lblMargin(left)=1
ModifyGraph margin(bottom)=60
ModifyGraph lblMargin(bottom)=1
ModifyGraph width={Aspect,1.6}
ModifyGraph height=200
DoWindow/C plotImage2
ModifyGraph mirror=1
ModifyGraph tick=2
SetAxis bottom 1486.5,1488.5

End
////////////////////////////////
Function test()
Display as"image";AppendImage dataDB20;DelayUpdate
ModifyImage dataDB20 ctab= {-45,*,Geo32,1}
ModifyGraph tick(bottom)=3
ModifyGraph noLabel(bottom)=2
NewFreeAxis /B wavelength
SetAxis wavelength 1483,1493
ModifyGraph manTick(wavelength)={1,2,0,0},manMinor(wavelength)={0,50}
ModifyGraph freePos(wavelength)=1
NewFreeAxis /R waveguide
SetAxis waveguide 1,11
ModifyGraph freePos(waveguide)=1
ColorScale/C/N=text0/A=MC  ctab={-45,-17,Geo32,1}
ColorScale/C/N=text0 "\F'Arial'\Z12Transmission (dB)"
ColorScale/C/N=text0 heightPct=60
ColorScale/C/N=text0/A=LT/X=1/Y=1
ModifyGraph manTick(waveguide)={0,1,0,0},manMinor(waveguide)={0,0}
ModifyGraph tickEnab(waveguide)={-inf,10}
ModifyGraph margin(right)=60
ModifyGraph margin(left)=70
ModifyGraph margin(bottom)=50
Label waveguide "\F'Arial'\Z18Output waveguide"
Label wavelength "\F'Arial'\Z18Wavelength (nm)"
Label left "\F'Arial'\Z18Channel"
ModifyGraph fSize(wavelength)=18,font(wavelength)="Arial"
ModifyGraph fSize(left)=18,font(left)="Arial"
ModifyGraph fSize(waveguide)=18,font(waveguide)="Arial"
ModifyGraph lblPos(wavelength)=48
ModifyGraph lblPos(waveguide)=60
ModifyGraph lblMargin(left)=10
SetAxis left -0.5,100
ModifyGraph width={Aspect,1.6}
ModifyGraph height=200
ModifyGraph tick(wavelength)=2
ModifyGraph tick(left)=2
ModifyGraph tick(waveguide)=2
ModifyGraph tick=2,mirror(bottom)=1



End





Function hsv2rgb(h,s,v)
	Variable h,s,v
	Variable rr,gg,bb
	Variable/G r,g,b
	Variable hi,f,p,q,t
	hi = mod(floor(h/60),6)
	f=h/60-floor(h/60)
	p=v*(1-s)
	q=v*(1-f*s)
	t=v*(1-(1-f)*s)
	switch(hi)
			case 0:
		rr=v
		gg=t
		bb=p
		break
			case 1:
		rr=q
		gg=v
		bb=p
		break
			case 2:
		rr=p
		gg=v
		bb=t
		break
			case 3:
		rr=p
		gg=q
		bb=v
		break
			case 4:
		rr=t
		gg=p
		bb=v
		break
			case 5:
		rr=v
		gg=p
		bb=q
		break
	default:
		break
	endswitch
	r=round(rr*65535)
	g=round(gg*65535)
	b=round(bb*65535)
End