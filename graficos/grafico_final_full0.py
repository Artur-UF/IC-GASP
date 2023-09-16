from __future__ import division
from subprocess import call
from math import *
from ROOT import *

#####################################################################
# GGS (CERN-CMS/UFRGS) ---
# the muons are collected considering the ID codes in the event
# sample produced with SuperCHICv2 in LHE format.
#####################################################################

#####################################################################
# USER INPUT:

# CROSS SECTION(S) (pb):
xsec    = [ 0.186818512E-03, 9.985100e-01, 0.13912579E+02, 1.5393433571E+00]; #FIXME
#xsec = [ 1. , 1. , 1. , 1. , .1 ];

# PDF "_"+LABEL FOR OUTPUT FILES:
JOB     = "histos";
PDF     = [ 'superchic', 'MadGraph', 'FPMC', 'LPAIR']; #FIXME
scale   = False; #bug, use False
cuts    = False;
setLog  = False;
filled  = False;
stacked = False;
data    = False;

# KINEMATICAL CUTS: #FIXME
INVMCUTUPPER = 150.0; # (NO CUT 9999.0 )
INVMCUTLOWER = 100.0; # (NO CUT 0.0)

PTPAIRCUTUPPER = 120.0; # (NO CUT 0.0 )
PTPAIRCUTLOWER = 0.0; # (NO CUT 0.0)

ETAPAIRCUT = 2.5; # (NO CUT 100.)
INNER = True; # (TRUE: -x < y < +x ; FALSE: y < -x AND y > +x)

PTCUTUPPER = 9999.0; # (NO CUT 9999.0 )
PTCUTLOWER = 0.0; # (NO CUT 0.0)

# INPUT FILES:

#processo 3
FILES   = [
"amostras/newevrectest.dat", 'amostras/newunweighted_events.lhe', 'amostras/Artur_gammagammamumu-fpmc_elel_pt0_14tev.lhe', 'amostras/Artur_gammagammamumu-lpair_elel_pt0_14tev.lhe']
#FIXME

# EVENT SAMPLE INPUT:
Nevt     = 10000; #FIXME
EVTINPUT = str(int(Nevt/1000))+"k";

#####################################################################

# LABELS:
STRING	= "";
for m in range(len(PDF)):
	if (PDF[m]==PDF[-1]):
		STRING+=PDF[m]+"_";
	else:
		STRING+=PDF[m]+"-";

LABEL = "FULL_inner.final.madgraph";
if cuts: LABEL+=".cuts";
if scale: LABEL+=".scaled";
if setLog: LABEL+=".log";
if filled: LABEL+=".filled";
if stacked: LABEL+=".stacked";
if data: LABEL+=".data";

# IMAGE FORMATS TO BE CREATED:
FILE_TYPES = [LABEL+".png"];
print ("*****");
print ("Os arquivos gravados em %s" % (FILE_TYPES[0]));
print ("*****");
# SAVING HISTOS INTO ROOT FILE:
FILEROOT = TFile("histos"+LABEL+".root","RECREATE");

# CREATE INDIVIDUAL DIRS FOR IMAGE TYPES:
#print(len(FILE_TYPES))
for l in range(len(FILE_TYPES)):
	call(["mkdir","-p",FILE_TYPES[l]]);

#####################################################################

# ARRAYS FOR EACH TYPE OF DISTRIBUTIONS:
#
# 1D:
'''invm_decay	= [];
pt_decay	= [];
ptsum_decay	= [];
eta_decay	= [];
phi_decay	= [];
E_decay		= [];
dpt_decay       = [];
acop            = [];
acop_zoom       = [];
dataonly        = [];
dphi            = [];
dphi_zoom       = [];'''
protpz          = [];
proten          = [];
protxi          = []
protpt          = []
mpp             = []
mupz           = []
muen           = []
mupt           = []
ivm_mu          = []
phopz           = []
phopt           = []
phoen           = []
# 3D:
DDDpt1pt2	= [];
DDDphi1phi2	= [];
DDDptsumphi	= [];
DDDpt1ptsum	= [];
DDDpt2ptsum	= [];
DDDmllptsum	= [];
DDDetaptsum	= [];
DDDetatheta	= [];
DDDetacost	= [];
DDDmllcost	= [];
DDDth1th2	= [];
# 2D:
DDpt1pt2	= [];
DDphi1phi2	= [];
DDptsumphi	= [];
DDpt1ptsum	= [];
DDpt2ptsum	= [];
DDmllptsum	= [];
DDetatheta	= [];
DDetacost	= [];
DDmllcost	= [];
DDth1th2	= [];

# SETTING THE NUMBER OF DIGITS ON AXIS
TGaxis.SetMaxDigits(2)

# SORTING THE DISTRIBUTIONS WITHIN THE SETS:
# THE ARRAYS STORE THE LABELS FOR AXIS AND UNITS:
histoslog        = [protpz,proten,protxi,protpt,mpp,mupz,muen,mupt,ivm_mu,phopz,phopt,phoen];
histoslog_label  = ["protpz","proten",'protxi','protpt','mpp',"mupz","muen","mupt",'ivm_mu','phopz','phopt','phoen'];
histoslog_axis   = ["p_{z}(p)","E(p)",'#chi(p)','p_{T}(p)','M(p^{+}p^{-})',"p_{z}(#mu)","E(#mu)","p_{T}(#mu)",'M(#mu^{+}#mu^{-})','p_{z}(#alpha)','p_{T}(#alpha)','E(#alpha)'];
histoslog_varx   = ["(GeV)","(GeV)",'','(GeV)','(GeV)',"(GeV)","(GeV)","(GeV)",'(GeV)','(GeV)','(GeV)','(GeV)'];


#histoslog        = [invm_decay,pt_decay,ptsum_decay,eta_ecay,phi_decay,E_decay,dpt_decay,acop,acop_zoom,dphi,dphi_zoom,protpz,proten, mupz];
#histoslog_label  = ["invm_decay","pt_decay","ptsum_decay","eta_decay","phi_decay","E_decay","dpt_decay","acop","acop_zoom","dphi","dphi_zoom","protpz","proten","mupz"];
#histoslog_axis   = ["M(x^{+}x^{-})","p_{T}(x^{#pm})","p_{T}(x^{+}x^{-})","#eta(x^{+}x^{-})","#phi(x^{+},x^{-})","E(x^{+},x^{-})","#Delta p_{T}(x^{+}x^{-})","1-|#Delta#phi(x^{+}x^{-})/#pi|","1-|#Delta#phi(x^{+}x^{-})/#pi|","|#Delta#phi(x^{+}x^{-})|","|#Delta#phi(x^{+}x^{-})|","p_{z}(p)","E(p)","p_{z}(m)"];
#histoslog_varx   = ["(GeV)","(GeV)","(GeV)","","","(GeV)","(GeV)","","","(deg)","(deg)","(GeV)","(GeV)","(GeV)"];

legoslog         = [DDDpt1pt2,DDDphi1phi2,DDDptsumphi,DDDpt1ptsum,DDDpt2ptsum,DDDmllptsum,DDDetaptsum,DDDetatheta,DDDetacost,DDDmllcost,DDDth1th2];
legoslog_label   = ["3Dpt1pt2","3Dphi1phi2","3Dptsumphi","3Dpt1ptsum","3Dpt2ptsum","3Dmllptsum","3Detaptsum","3Detatheta","3Detacost","3Dmllcost","3Dth1th2"];
legoslog_xaxis   = ["p_{T}(x^{+})","#phi(x^{+})","p_{T}(x^{+}x^{-})","p_{T}(x^{#pm})","p_{T}(x^{#pm})","M(x^{+}x^{-})","#eta(x^{+}x^{-})","#eta(x^{+}x^{-})","#eta(x^{+}x^{-})","M(x^{+}x^{-})","#theta_{1}"];
legoslog_yaxis   = ["p_{T}(x^{-})","#phi(x^{-})","#phi(x^{#pm})","p_{T}(x^{+}x^{-})","p_{T}(x^{+}x^{-})","p_{T}(x^{+}x^{-})","p_{T}(x^{+}x^{-})","#theta(x^{+}x^{-})","cos#theta(x^{+}x^{-})","cos#theta(x^{+}x^{-})","#theta_{2}"];
legoslog_varz    = ["(nb/GeV^{2})","(nb)","(nb/GeV*deg)","(nb/GeV^{2})","(nb/GeV^{2})","(nb/GeV^{2})","(nb/GeV^{2})","(nb/deg)","(nb)","(nb/GeV)","(nb)"];
legoslog_varx    = ["(GeV)","(deg)","(GeV)","(GeV)","(GeV)","(GeV)","","","","(GeV)","(deg)"];
legoslog_vary    = ["(GeV)","(deg)","","(GeV)","(GeV)","(GeV)","(GeV)","(deg)","","","(deg)"];

DDlog         = [DDpt1pt2,DDphi1phi2,DDptsumphi,DDpt1ptsum,DDpt2ptsum,DDmllptsum,DDetatheta,DDetacost,DDmllcost,DDth1th2];
DDlog_label   = ["2Dpt1pt2","2Dphi1phi2","2Dptsumphi","2Dpt1ptsum","2Dpt2ptsum","2Dmllptsum","2Detatheta","2Detacost","2Dmllcost","2Dth1th2"];
DDlog_xaxis   = ["p_{T}(x^{+})","#phi(x^{+})","p_{T}(x^{+}x^{-})","p_{T}(x^{+})","p_{T}(x^{-})","M(x^{+}x^{-})","#eta(x^{+}x^{-})","#eta(x^{+}x^{-})","M(x^{+}x^{-})","#theta_{1}"];
DDlog_yaxis   = ["p_{T}(x^{-})","#phi(x^{-})","#phi(x^{#pm})","p_{T}(x^{+}x^{-})","p_{T}(x^{+}x^{-})","p_{T}(x^{+}x^{-})","#theta(x^{+}x^{-})","cos#theta(x^{+}x^{-})","cos#theta(x^{+}x^{-})","#theta_{2}"];
DDlog_varx    = ["(GeV)","(deg)","(GeV)","(GeV)","(GeV)","(GeV)","","","(GeV)","(deg)"];
DDlog_vary    = ["(GeV)","(deg)","","(GeV)","(GeV)","(GeV)","(deg)","","","(deg)"];

# STARTING THE LOOP OVER FILES:
for i in range(len(FILES)):
    f = open(FILES[i],'r');
    print (f"Opening file {i}: {FILES[i]}");

    # SORTING THE DISTRIBUTIONS IN THE ARRAYS FOR EACH FILE:
    # EACH ARRAYS IS FORMATTED LIKE: array[] = [plots_file1, plots_file2, plots_file3, ...
    #invm_decay.append(TH1D("1D_invm_decay"+"_"+PDF[i],"", 50,  20., 350.));
    #pt_decay.append(TH1D("1D_pt_decay"+"_"+PDF[i]	, "", 50,  0., 200.));
    #ptsum_decay.append(TH1D("1D_ptsum_decay"+"_"+PDF[i], "", 50,  0., 360.));
    #eta_decay.append(TH1D("1D_eta_decay"+"_"+PDF[i]	, "", 50,-10.,  10.));
    #phi_decay.append(TH1D("1D_phi_decay"+"_"+PDF[i]	, "", 10, -4.,   4.));
    #E_decay.append(TH1D("1D_E_decay"+"_"+PDF[i]	, "", 50,  0., 250.));
    #dpt_decay.append(TH1D("1D_dpt_decay"+"_"+PDF[i] , "", 50,  0.,   0.1));
    #acop.append(TH1D("1D_acop"+"_"+PDF[i]           , "", 50,  0.,  10.));
    #acop_zoom.append(TH1D("1D_acopz"+"_"+PDF[i]     , "", 50,  -.01,   1.));
    #dphi.append(TH1D("1D_dphi"+"_"+PDF[i]           , "", 50,  0., 181.));
    #dphi_zoom.append(TH1D("1D_dphiz"+"_"+PDF[i]     , "", 50,175., 180.1));
    protpz.append(TH1D("1D_protpz"+"_"+PDF[i]       , "", 50,4300., 7200.))
    proten.append(TH1D("1D_proten"+"_"+PDF[i]       , "", 50,4300., 7200.))
    protxi.append(TH1D("1D_protxi"+"_"+PDF[i]       , "", 50,-0.01,0.05))
    protpt.append(TH1D("1D_protpt"+"_"+PDF[i]       , "", 50,-0.1, 1.))
    mpp.append(TH1D("1D_mpp"+"_"+PDF[i]       , "", 50,-20., 700.))
    mupz.append(TH1D("1D_mupz"+"_"+PDF[i]       , "", 50,-2500.,2500.))
    muen.append(TH1D("1D_muen"+"_"+PDF[i]       , "", 50,-100., 900.))
    mupt.append(TH1D("1D_mupt"+"_"+PDF[i]       , "", 50,-5., 40.0))
    ivm_mu.append(TH1D("1D_ivm_mu"+"_"+PDF[i]       , "", 50,0., 50.0))
    phopz.append(TH1D("1D_phopz"+"_"+PDF[i]       , "", 50,4973., 4980.))
    phopt.append(TH1D("1D_phopt"+"_"+PDF[i]       , "", 50,0., 500.))
    phoen.append(TH1D("1D_phoen"+"_"+PDF[i]       , "", 50,-100., 2000.))
    #mopz.append(TH1D("1D_mupz"+"_"+PDF[i]       , "", 50,-2500.,2500.))
    #moen.append(TH1D("1D_muen"+"_"+PDF[i]       , "", 50,-100., 900.))
    #mopt.append(TH1D("1D_mupt"+"_"+PDF[i]       , "", 50,-5., 40.0))
    #DDDpt1pt2.append(TH2D("3D_pt1_pt2_"+PDF[i]      , "", 50,  0.,  70., 50, 0.,  70.));
    #DDDphi1phi2.append(TH2D("3D_phi1_phi2_"+PDF[i]  , "", 45,  0., 180., 45, 0., 180.));
    #DDDptsumphi.append(TH2D("3D_ptsum_phi_"+PDF[i]	, "", 50,  0., 160., 45, 0., 180.));
    #DDDpt1ptsum.append(TH2D("3D_pt1_ptsum_"+PDF[i]	, "", 50,  0.,  80., 50, 0., 120.));
    #DDDpt2ptsum.append(TH2D("3D_pt2_ptsum_"+PDF[i]	, "", 50,  0.,  80., 50, 0., 120.));
    #DDDmllptsum.append(TH2D("3D_mll_ptsum_"+PDF[i]	, "", 50,  0., 140., 50, 0., 120.));
    #DDDetaptsum.append(TH2D("3D_eta_ptsum_"+PDF[i]	, "", 50,-15.,  15., 50, 0., 100.));
    #DDDetatheta.append(TH2D("3D_eta_theta_"+PDF[i]  , "", 50,-10.,  10., 45, 0., 180.));
    #DDDetacost.append(TH2D("3D_eta_cost_"+PDF[i]    , "", 50,-15.,  15., 50,-1.,   1.));
    #DDDmllcost.append(TH2D("3D_mll_cost_"+PDF[i]    , "", 50,  0., 300., 50,-1.,   1.));
    #DDDth1th2.append(TH2D("3D_th1_th2_"+PDF[i]      , "", 45,  0., 180., 45, 0., 180.));
    #DDpt1pt2.append(TH2D("2D_pt1_pt2_"+PDF[i]       , "", 50,  0.,  60., 50, 0.,  60.));
    #DDphi1phi2.append(TH2D("2D_phi1_phi2_"+PDF[i]   , "", 45,  0., 180., 45, 0., 180.));
    #DDptsumphi.append(TH2D("2D_ptsum_phi_"+PDF[i] 	, "", 50,  0., 120., 45, 0., 180.));
    #DDpt1ptsum.append(TH2D("2D_pt1_ptsum_"+PDF[i] 	, "", 50,  0.,  60., 50, 0., 120.));
    #DDpt2ptsum.append(TH2D("2D_pt2_ptsum_"+PDF[i] 	, "", 50,  0.,  60., 50, 0., 100.));
    #DDmllptsum.append(TH2D("2D_mll_ptsum_"+PDF[i] 	, "", 50,  0., 140., 50, 0., 140.));
    #DDetatheta.append(TH2D("2D_eta_theta_"+PDF[i]   , "", 50,-10.,  10., 45, 0., 180.));
    #DDetacost.append(TH2D("2D_eta_cost_"+PDF[i]     , "", 50,-10.,  10., 50,-1.,   1.));
    #DDmllcost.append(TH2D("2D_mll_cost_"+PDF[i]     , "", 50,  0., 180., 50,-1.,   1.));
    #DDth1th2.append(TH2D("2D_th1_th2_"+PDF[i]       , "", 45,  0., 180., 45, 0., 180.));

    # LOOP OVER LINES IN LHE SAMPLE:

    # RESET EVENT COUNTING:
    event  = 0;
    evPASS = 0;
    # START LOOP:
    '''if (i == 0):
    	for j in xrange(434): # skip first 434 lines to avoid MG5 comments
            	f.readline();
    else:
                for j in xrange(440): # skip first 500 lines to avoid MG5 comments
                        f.readline();'''
    if (i == 0):
        for j in range(88): # skip first 434 lines to avoid MG5 comments
            f.readline()
    elif (i == 1):
        for j in range(371): # skip first 431 lines to avoid MG5 comments
            f.readline()
    elif (i == 2):
        for j in range(430): # skip first 430 lines to avoid MG5 comments
            f.readline()
    elif (i == 3):
        for j in range(440): # skip first 440 lines to avoid MG5 comments
            f.readline();
    for line in f:
        # SKIP BLANK LINES:
        line = line.strip();
        if not line: continue;
        # STORE LINES INTO ARRAY:
        coll = line.split();
        # READ EVENT CONTENT:
        if coll[0] == "<event>":
            event += 1;
            # SET A SCREEN OUTPUT FOR CONTROL:
            if Nevt < 10000: evtsplit = 1000;
            else: evtsplit = 10000;
            perct = event / Nevt * 100.;
            if event%evtsplit==0: print ("Event %i [%.2f%%]" % (event,perct));
            elif event>Nevt: break;
        # 4-VECTORS FOR DECAY PRODUCTS:
        elif coll[0] == '22' and eval(coll[8]) > 0:
            dp = TLorentzVector();
            px = float(coll[6]);
            py = float(coll[7]);
            pz = float(coll[8]);
            en = float(coll[9]);
            dp.SetPxPyPzE(px,py,pz,en);
        elif coll[0] == '22' and eval(coll[8]) < 0:
            dm = TLorentzVector();
            px = float(coll[6]);
            py = float(coll[7]);
            pz = float(coll[8]);
            en = float(coll[9]);
            dm.SetPxPyPzE(px,py,pz,en);
        elif coll[0] == '13' and coll[1] == '1':
            dmu = TLorentzVector();
            px = float(coll[6]);
            py = float(coll[7]);
            pz = float(coll[8]);
            en = float(coll[9]);
            dmu.SetPxPyPzE(px,py,pz,en);
        elif coll[0] == '-13' and coll[1] == '1':
            damu = TLorentzVector();
            px = float(coll[6]);
            py = float(coll[7]);
            pz = float(coll[8]);
            en = float(coll[9]);
            damu.SetPxPyPzE(px,py,pz,en);
        elif coll[0] == '90':
            dmo = TLorentzVector();
            px = float(coll[6]);
            py = float(coll[7]);
            pz = float(coll[8]);
            en = float(coll[9]);
            dmo.SetPxPyPzE(px,py,pz,en);
        elif coll[0] == '2212' and coll[1] == '1' and eval(coll[8]) > 0 and abs(eval(coll[8])) < 7000:
            dpp = TLorentzVector();
            px = float(coll[6]);
            py = float(coll[7]);
            pz = float(coll[8]);
            en = float(coll[9]);
            dpp.SetPxPyPzE(px,py,pz,en);
        elif coll[0] == '2212' and coll[1] == '1' and eval(coll[8]) < 0 and abs(eval(coll[8])) < 7000:
            dpm = TLorentzVector();
            px = float(coll[6]);
            py = float(coll[7]);
            pz = float(coll[8]);
            en = float(coll[9]);
            dpm.SetPxPyPzE(px,py,pz,en);
        # CLOSE EVENT AND FILL HISTOGRAMS:
        #print ("OI 2");
        elif coll[0] == "</event>":
            # KINEMATICS OF DECAY PRODUCTS:
            if ( cuts and INNER
                and (dp+dm).M() >= INVMCUTLOWER
                and (dp+dm).M() <= INVMCUTUPPER
                and (dp+dm).Pt() >= PTPAIRCUTLOWER
        	    and (dp+dm).Pt() <= PTPAIRCUTUPPER
                and abs((dp+dm).Eta()) <= ETAPAIRCUT
                and dp.Pt() >= PTCUTLOWER
                and dm.Pt() >= PTCUTLOWER
                and dp.Pt() <= PTCUTUPPER
                and dm.Pt() <= PTCUTUPPER):
                # 1D:
                invm_decay[i].Fill((dp+dm).M());
                pt_decay[i].Fill(dp.Pt());
                pt_decay[i].Fill(dm.Pt());
                ptsum_decay[i].Fill((dp+dm).Pt());
                eta_decay[i].Fill((dp).Eta());
                eta_decay[i].Fill((dm).Eta());
                phi_decay[i].Fill(dp.Phi());
                phi_decay[i].Fill(dm.Phi());
                E_decay[i].Fill(dp.E());
                E_decay[i].Fill(dm.E());
                dpt_decay[i].Fill(abs(dp.Pt()-dm.Pt()));
                dphi[i].Fill(abs(dp.DeltaPhi(dm))*180./3.141592);
                dphi_zoom[i].Fill(abs(dp.DeltaPhi(dm))*180./3.141592);
                acop_zoom[i].Fill((1. - abs(dp.DeltaPhi(dm))/3.141592));
                acop[i].Fill((1. - abs(dp.DeltaPhi(dm))/3.141592));
                # 3D:
                DDDetaptsum[i].Fill((dp+dm).Eta(),(dp+dm).Pt());
                DDDmllcost[i].Fill((dp+dm).M(),(dp+dm).CosTheta());
                DDDpt1pt2[i].Fill(dp.Pt(),dm.Pt());
                DDDphi1phi2[i].Fill(dp.Phi()*180./3.141592,dm.Phi()*180./3.141592);
                DDDpt1ptsum[i].Fill(dp.Pt(),(dp+dm).Pt());
                DDDpt2ptsum[i].Fill(dm.Pt(),(dp+dm).Pt());
                DDDmllptsum[i].Fill((dp+dm).M(),(dp+dm).Pt());
                DDDptsumphi[i].Fill((dp+dm).Pt(),dp.Phi()*180./3.141592);
                DDDptsumphi[i].Fill((dp+dm).Pt(),dm.Phi()*180./3.141592);
                DDDetatheta[i].Fill((dp+dm).Eta(),(dp+dm).Theta()*180./3.141592);
                DDDetacost[i].Fill((dp+dm).Eta(),(dp+dm).CosTheta());
                DDDth1th2[i].Fill(dp.Theta()*180./3.141592,dm.Theta()*180./3.141592);
                # 2D:
                DDpt1pt2[i].Fill(dp.Pt(),dm.Pt());
                DDphi1phi2[i].Fill(dp.Phi()*180./3.141592,dm.Phi()*180./3.141592);
                DDpt1ptsum[i].Fill(dp.Pt(),(dp+dm).Pt());
                DDpt2ptsum[i].Fill(dm.Pt(),(dp+dm).Pt());
                DDmllptsum[i].Fill((dp+dm).M(),(dp+dm).Pt());
                DDptsumphi[i].Fill((dp+dm).Pt(),dp.Phi()*180./3.141592);
                DDDetacost[i].Fill((dp+dm).Eta(),(dp+dm).CosTheta());
                DDDth1th2[i].Fill(dp.Theta()*180./3.141592,dm.Theta()*180./3.141592);
                # 2D:
                DDpt1pt2[i].Fill(dp.Pt(),dm.Pt());
                DDphi1phi2[i].Fill(dp.Phi()*180./3.141592,dm.Phi()*180./3.141592);
                DDpt1ptsum[i].Fill(dp.Pt(),(dp+dm).Pt());
                DDpt2ptsum[i].Fill(dm.Pt(),(dp+dm).Pt());
                DDmllptsum[i].Fill((dp+dm).M(),(dp+dm).Pt());
                DDptsumphi[i].Fill((dp+dm).Pt(),dp.Phi()*180./3.141592);
                DDptsumphi[i].Fill((dp+dm).Pt(),dm.Phi()*180./3.141592);
                DDetatheta[i].Fill((dp+dm).Eta(),(dp+dm).Theta()*180./3.141592);
                DDetacost[i].Fill((dp+dm).Eta(),(dp+dm).CosTheta());
                DDmllcost[i].Fill((dp+dm).M(),(dp+dm).CosTheta());
                DDth1th2[i].Fill(dp.Theta()*180./3.141592,dm.Theta()*180./3.141592);
                evPASS += 1;
            elif ( cuts and not INNER
                and (dp+dm).M() >= INVMCUTLOWER
                and (dp+dm).M() <= INVMCUTUPPER
                and (dp+dm).Pt() >= PTPAIRCUTLOWER
                and (dp+dm).Pt() <= PTPAIRCUTUPPER
                and abs((dp+dm).Eta()) >= ETAPAIRCUT
                and dp.Pt() >= PTCUTLOWER
                and dm.Pt() >= PTCUTLOWER
                and dp.Pt() <= PTCUTUPPER
                and dm.Pt() <= PTCUTUPPER):
                # 1D:
                invm_decay[i].Fill((dp+dm).M());# !
                pt_decay[i].Fill(dp.Pt());
                pt_decay[i].Fill(dm.Pt());
                ptsum_decay[i].Fill((dp+dm).Pt());
                eta_decay[i].Fill((dp).Eta());
                eta_decay[i].Fill((dm).Eta());
                phi_decay[i].Fill(dp.Phi());
                phi_decay[i].Fill(dm.Phi());
                E_decay[i].Fill(dp.E());
                E_decay[i].Fill(dm.E());
                dpt_decay[i].Fill(abs(dp.Pt()-dm.Pt()));
                dphi[i].Fill(abs(dp.DeltaPhi(dm))*180./3.141592);
                dphi_zoom[i].Fill(abs(dp.DeltaPhi(dm))*180./3.141592);
                acop_zoom[i].Fill((1. - abs(dp.DeltaPhi(dm))/3.141592));
                acop[i].Fill((1. - abs(dp.DeltaPhi(dm))/3.141592));
                # 3D:
                DDDetaptsum[i].Fill((dp+dm).Eta(),(dp+dm).Pt());
                DDDmllcost[i].Fill((dp+dm).M(),(dp+dm).CosTheta());
                DDDpt1pt2[i].Fill(dp.Pt(),dm.Pt());
                DDDphi1phi2[i].Fill(dp.Phi()*180./3.141592,dm.Phi()*180./3.141592);
                DDDpt1ptsum[i].Fill(dp.Pt(),(dp+dm).Pt());
                DDDpt2ptsum[i].Fill(dm.Pt(),(dp+dm).Pt());
                DDDmllptsum[i].Fill((dp+dm).M(),(dp+dm).Pt());
                DDDptsumphi[i].Fill((dp+dm).Pt(),dp.Phi()*180./3.141592);
                DDDptsumphi[i].Fill((dp+dm).Pt(),dm.Phi()*180./3.141592);
                DDDetatheta[i].Fill((dp+dm).Eta(),(dp+dm).Theta()*180./3.141592);
                DDDetacost[i].Fill((dp+dm).Eta(),(dp+dm).CosTheta());
                DDDth1th2[i].Fill(dp.Theta()*180./3.141592,dm.Theta()*180./3.141592);
                # 2D:
                DDpt1pt2[i].Fill(dp.Pt(),dm.Pt());
                DDphi1phi2[i].Fill(dp.Phi()*180./3.141592,dm.Phi()*180./3.141592);
                DDpt1ptsum[i].Fill(dp.Pt(),(dp+dm).Pt());
                DDpt2ptsum[i].Fill(dm.Pt(),(dp+dm).Pt());
                DDmllptsum[i].Fill((dp+dm).M(),(dp+dm).Pt());
                DDptsumphi[i].Fill((dp+dm).Pt(),dp.Phi()*180./3.141592);
                DDptsumphi[i].Fill((dp+dm).Pt(),dm.Phi()*180./3.141592);
                DDetatheta[i].Fill((dp+dm).Eta(),(dp+dm).Theta()*180./3.141592);
                DDetacost[i].Fill((dp+dm).Eta(),(dp+dm).CosTheta());
                DDmllcost[i].Fill((dp+dm).M(),(dp+dm).CosTheta());
                DDth1th2[i].Fill(dp.Theta()*180./3.141592,dm.Theta()*180./3.141592);
                evPASS += 1;
            elif not cuts:
                # 1D:
                #-------------------------Medidas dos prótons
                protpz[i].Fill(dpp.Pz());
                protpz[i].Fill(dpm.Pz());
                proten[i].Fill(dpp.E())
                proten[i].Fill(dpm.E())
                protxi[i].Fill(1-(dpp.Pz()/7000))
                protxi[i].Fill(1-(dpm.Pz()/(-7000)))
                mpp[i].Fill(sqrt((1-(dpp.Pz()/7000))*(1-(dpm.Pz()/(-7000))))*7000)
                protpt[i].Fill(sqrt(dpp.Px()**2 + dpp.Py()**2))
                protpt[i].Fill(sqrt(dpm.Px()**2 + dpm.Py()**2))
                #-------------------------Medidas dos Múons
                mupz[i].Fill(dmu.Pz())
                muen[i].Fill(dmu.E())
                muen[i].Fill(damu.E())
                mupt[i].Fill(dmu.Pt())
                mupt[i].Fill(damu.Pt())
                ivm_mu[i].Fill((dmu+damu).M())
                #-------------------------Medidas dos fótons
                phopt[i].Fill(dp.Pt())
                phopt[i].Fill(dm.Pt())
                phopz[i].Fill(dp.Pz())
                phopz[i].Fill(dm.Pz())
                phoen[i].Fill(dm.E())
                phoen[i].Fill(dp.E())
                #-------------------------Medidas do monopolo
                #mopz[i].Fill(dmo.Pz())
                #moen[i].Fill(dmo.E())
                #mopt[i].Fill(dmo.Pt())
                '''
                invm_decay[i].Fill((dp+dm).M());
                pt_decay[i].Fill(dp.Pt());
                pt_decay[i].Fill(dm.Pt());
                ptsum_decay[i].Fill((dp+dm).Pt());
                eta_decay[i].Fill((dp).Eta());
                eta_decay[i].Fill((dm).Eta());
                phi_decay[i].Fill(dp.Phi());
                phi_decay[i].Fill(dm.Phi());
                E_decay[i].Fill(dp.E());
                E_decay[i].Fill(dm.E());
                dpt_decay[i].Fill(abs(dp.Pt()-dm.Pt()));
                dphi[i].Fill(abs(dp.DeltaPhi(dm))*180./3.141592);
                dphi_zoom[i].Fill(abs(dp.DeltaPhi(dm))*180./3.141592);
                #print ("%f" % abs(dp.Pt()-dm.Pt()));
                acop_zoom[i].Fill((1. - abs(dp.DeltaPhi(dm))/3.141592));
                acop[i].Fill((1. - abs(dp.DeltaPhi(dm))/3.141592));
                #if (i ==0): print ("%f" % abs(1. - abs(dp.DeltaPhi(dm))/3.141592));
                #print ("%f" % float(dp.DeltaPhi(dm)));
                # 3D:
                DDDetaptsum[i].Fill((dp+dm).Eta(),(dp+dm).Pt());
                DDDmllcost[i].Fill((dp+dm).M(),(dp+dm).CosTheta());
                DDDpt1pt2[i].Fill(dp.Pt(),dm.Pt());
                DDDphi1phi2[i].Fill(dp.Phi()*180./3.141592,dm.Phi()*180./3.141592);
                DDDpt1ptsum[i].Fill(dp.Pt(),(dp+dm).Pt());
                DDDpt2ptsum[i].Fill(dm.Pt(),(dp+dm).Pt());
                DDDmllptsum[i].Fill((dp+dm).M(),(dp+dm).Pt());
                DDDptsumphi[i].Fill((dp+dm).Pt(),dp.Phi()*180./3.141592);
                DDDptsumphi[i].Fill((dp+dm).Pt(),dm.Phi()*180./3.141592);
                DDDetatheta[i].Fill((dp+dm).Eta(),(dp+dm).Theta()*180./3.141592);
                DDDetacost[i].Fill((dp+dm).Eta(),(dp+dm).CosTheta());
                DDDth1th2[i].Fill(dp.Theta()*180./3.141592,dm.Theta()*180./3.141592);
                # 2D:
                DDpt1pt2[i].Fill(dp.Pt(),dm.Pt());
                DDphi1phi2[i].Fill(dp.Phi()*180./3.141592,dm.Phi()*180./3.141592);
                DDpt1ptsum[i].Fill(dp.Pt(),(dp+dm).Pt());
                DDpt2ptsum[i].Fill(dm.Pt(),(dp+dm).Pt());
                DDmllptsum[i].Fill((dp+dm).M(),(dp+dm).Pt());
                DDptsumphi[i].Fill((dp+dm).Pt(),dp.Phi()*180./3.141592);
                DDptsumphi[i].Fill((dp+dm).Pt(),dm.Phi()*180./3.141592);
                DDetatheta[i].Fill((dp+dm).Eta(),(dp+dm).Theta()*180./3.141592);
                DDetacost[i].Fill((dp+dm).Eta(),(dp+dm).CosTheta());
                DDmllcost[i].Fill((dp+dm).M(),(dp+dm).CosTheta());
                DDth1th2[i].Fill(dp.Theta()*180./3.141592,dm.Theta()*180./3.141592);
        # End of loop over lines'''
        if cuts: print ("Events passing acceptance: %i/%i" % (evPASS,event));
        #print ("Integral of %s: %.6f nb" % (PDF[i],evPASS*xsec[i]/event));
# End of loop over files

# Starting Drawing step:

# Defining the top label in the plots:
plotlabel = TPaveText(0.50,0.91,0.84,0.95,"NDC");
plotlabel.SetTextAlign(33);
plotlabel.SetTextColor(1);
plotlabel.SetFillColor(0);
plotlabel.SetBorderSize(0);
plotlabel.SetTextSize(0.035);
plotlabel.SetTextFont(42);
plotlabel.AddText("MadGraphv5 #bullet #sqrt{s}=14 TeV #bullet "+EVTINPUT+" evt");

# Legend:
leg = TLegend(0.55,0.72,0.75,0.87);
leg.SetTextSize(0.035);
leg.SetFillColor(0);
leg.SetBorderSize(0);

# Setting pads:
gStyle.SetOptStat(0);
gStyle.SetPadTickY(1);
gStyle.SetPadTickX(1);
gStyle.SetOptTitle(0);
gStyle.SetLegendBorderSize(0);

# Canvas
canvas = TCanvas("plots","Plots",0,0,700,860);

for i in range(len(histoslog)):
    globals()["hs_histoslog"+str(i)] = THStack("hs","");

# Starting loop over histograms in the arrays for each set:

# 1: 1D log-scaled plots:
canvas.SetLeftMargin(0.2);
canvas.SetBottomMargin(0.11);
canvas.SetRightMargin(0.18);
if setLog: gPad.SetLogy(1);
else: gPad.SetLogy(0);
legs=0;
for l in range(len(histoslog)):
    for m in range(len(FILES)):
            if scale:
                    histoslog[l][m].Scale(xsec[m]/Nevt*histoslog[l][m].GetBinWidth(1));
            histoslog[l][m].SetLineColor(m+1);
            if (m == 4): histoslog[l][m].SetLineColor(m+2);
            if filled:
                    histoslog[l][m].SetFillColor(m+1);
                    if (m == 4): histoslog[l][m].SetFillColor(m+2);
            histoslog[l][m].SetLineWidth(3);
            histoslog[l][m].SetLineStyle(1);
            globals()["hs_histoslog"+str(l)].Add(histoslog[l][m]);
            leg.AddEntry(histoslog[l][m]," "+PDF[m],"f");
            if data:
                if m == 0:
                        datapoints = histoslog[l][m].Clone();
                        dataonly = histoslog[l][m].Clone();
                else:
                        datapoints.Add(histoslog[l][m]);
                        dataonly.Add(histoslog[l][m]);
                        datapoints.SetFillStyle(0);
                        datapoints.SetLineWidth(0);
                        datapoints.SetLineStyle(0);
                        datapoints.SetMarkerStyle(20);
    if stacked:
            globals()["hs_histoslog"+str(l)].Draw("");
    else:
            globals()["hs_histoslog"+str(l)].Draw("nostack hist");
    if scale:
            globals()["hs_histoslog"+str(l)].GetYaxis().SetTitle("d#sigma/d"+str(histoslog_axis[l])+str(histoslog_varx[l])+" (pb)");
    else:
            globals()["hs_histoslog"+str(l)].GetYaxis().SetTitle("Events");
    globals()["hs_histoslog"+str(l)].GetXaxis().SetTitle(str(histoslog_axis[l])+" "+str(histoslog_varx[l]));
    globals()["hs_histoslog"+str(l)].GetXaxis().SetTitleFont(42);
    globals()["hs_histoslog"+str(l)].GetYaxis().SetTitleFont(42);
    globals()["hs_histoslog"+str(l)].GetXaxis().SetTitleSize(0.05);
    globals()["hs_histoslog"+str(l)].GetYaxis().SetTitleSize(0.05);
    globals()["hs_histoslog"+str(l)].GetXaxis().SetLabelFont(42);
    globals()["hs_histoslog"+str(l)].GetYaxis().SetLabelFont(42);
    globals()["hs_histoslog"+str(l)].GetXaxis().SetTitleOffset(1.);
    globals()["hs_histoslog"+str(l)].GetYaxis().SetTitleOffset(1.6);
    globals()["hs_histoslog"+str(l)].GetXaxis().SetLabelSize(0.04);
    globals()["hs_histoslog"+str(l)].GetYaxis().SetLabelSize(0.04);
    globals()["hs_histoslog"+str(l)].GetXaxis().SetDecimals(True);
    if data:
            datapoints.Draw("E2,SAME");
            leg.AddEntry(datapoints,"data","p");
    leg.Draw("SAME");
    plotlabel.Draw("SAME");
    for k in range(len(FILE_TYPES)):
    	canvas.Print(FILE_TYPES[k]+"/"+JOB+"_"+EVTINPUT+"evt_"+histoslog_label[l]+"."+FILE_TYPES[k]);
    leg.Clear();
    if data:
        dataonly.SetLineStyle(2);
        dataonly.SetFillColor(0);
        dataonly.SaveAs(FILE_TYPES[k]+"/"+JOB+"_"+EVTINPUT+"evt_"+histoslog_label[l]+".root");
