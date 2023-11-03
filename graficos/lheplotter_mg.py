#!/usr/bin/env python

from __future__ import division
from subprocess import call
from math import *
from ROOT import *

#####################################################################
# GGS (GAME/UFPel) ---
# the muons are collected considering the ID codes in the event
# sample produced with SuperCHICv2 in LHE format.
#####################################################################

#####################################################################
# USER INPUT:

# CROSS SECTION(S) (pb):
xsec    = [ 1. , 1. ]; #FIXME

# PDF "_"+LABEL FOR OUTPUT FILES:
JOB     = "histos";
PDF     = [ '' , ''  ]; #FIXME
scale   = False;
cuts    = False;
setLog  = False;

# KINEMATICAL CUTS:
INVMCUTUPPER = 350.0; # (NO CUT 9999.0 )
INVMCUTLOWER = 0.0; # (NO CUT 0.0)

PTPAIRCUTUPPER = 120.0; # (NO CUT 0.0 )
PTPAIRCUTLOWER = 0.0; # (NO CUT 0.0)

ETAPAIRCUT = 2.5; # (NO CUT 100.)
INNER = True; # (TRUE: -x < y < +x ; FALSE: y < -x AND y > +x)

PTCUTUPPER = 9999.0; # (NO CUT 9999.0 )
PTCUTLOWER = 0.0; # (NO CUT 0.0)

# INPUT FILES:

#processo 3
FILES   = [
"",
""
        ]; #FIXME

# EVENT SAMPLE INPUT:
EVTINPUT = "100k"; #FIXME
Nevt	 = 100000; #FIXME

#####################################################################

# LABELS:
STRING	= "";
for m in range(len(PDF)):
	if (PDF[m]==PDF[-1]):
		STRING+=PDF[m]+"_";
	else:
		STRING+=PDF[m]+"-";

LABEL = "final-madgraph";
if INNER: LABEL+="-inner"
if cuts: LABEL+="-cuts";
if scale: LABEL+="-scaled";
if setLog: LABEL+="-log";

# IMAGE FORMATS TO BE CREATED:
FILE_TYPES = [LABEL+".png"];
print "*****";
print "Os arquivos gravados em %s" % (FILE_TYPES[0]);
print "*****";
print "\n";
# SAVING HISTOS INTO ROOT FILE:
FILEROOT = TFile("histos.root","RECREATE");

# CREATE INDIVIDUAL DIRS FOR IMAGE TYPES:
for l in range(len(FILE_TYPES)):
	call(["mkdir","-p",FILE_TYPES[l]]);

#####################################################################

# ARRAYS FOR EACH TYPE OF DISTRIBUTIONS:
#
# 1D:
invm_decay	= [];
pt_decay	= [];
ptsum_decay	= [];
eta_decay	= [];
phi_decay	= [];
E_decay		= [];
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

# SORTING THE DISTRIBUTIONS WITHIN THE SETS:
# THE ARRAYS STORE THE LABELS FOR AXIS AND UNITS:
histoslog        = [invm_decay,pt_decay,ptsum_decay,eta_decay,phi_decay,E_decay];
histoslog_label  = ["invm_decay","pt_decay","ptsum_decay","eta_decay","phi_decay","E_decay"];
histoslog_axis   = ["M(x^{+}x^{-})","p_{T}(x^{#pm})","p_{T}(x^{+}x^{-})","#eta(x^{+}x^{-})","#phi(x^{+},x^{-})","E(x^{+},x^{-})"];
histoslog_varx   = ["(GeV)","(GeV)","(GeV)","","","(GeV)"];

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
        print "Opening file %i: %s" % (i,FILES[i]);

	# SORTING THE DISTRIBUTIONS IN THE ARRAYS FOR EACH FILE:
	# EACH ARRAYS IS FORMATTED LIKE: array[] = [plots_file1, plots_file2, plots_file3, ...
	invm_decay.append(TH1D("1D_invm_decay"+"_"+PDF[i],"", 50,  100., 350.));
	pt_decay.append(TH1D("1D_pt_decay"+"_"+PDF[i]	, "", 50,  0., 200.));
	ptsum_decay.append(TH1D("1D_ptsum_decay"+"_"+PDF[i], "", 50,  0., 360.));
        eta_decay.append(TH1D("1D_eta_decay"+"_"+PDF[i]	, "", 50,-10.,  10.));
        phi_decay.append(TH1D("1D_phi_decay"+"_"+PDF[i]	, "", 10, -4.,   4.));
        E_decay.append(TH1D("1D_E_decay"+"_"+PDF[i]	, "", 50,  0., 250.));
        DDDpt1pt2.append(TH2D("3D_pt1_pt2_"+PDF[i]      , "", 50,  0.,  70., 50, 0.,  70.));
        DDDphi1phi2.append(TH2D("3D_phi1_phi2_"+PDF[i]  , "", 45,  0., 180., 45, 0., 180.));
        DDDptsumphi.append(TH2D("3D_ptsum_phi_"+PDF[i]	, "", 50,  0., 160., 45, 0., 180.));
        DDDpt1ptsum.append(TH2D("3D_pt1_ptsum_"+PDF[i]	, "", 50,  0.,  80., 50, 0., 120.));
        DDDpt2ptsum.append(TH2D("3D_pt2_ptsum_"+PDF[i]	, "", 50,  0.,  80., 50, 0., 120.));
        DDDmllptsum.append(TH2D("3D_mll_ptsum_"+PDF[i]	, "", 50,  0., 140., 50, 0., 120.));
	DDDetaptsum.append(TH2D("3D_eta_ptsum_"+PDF[i]	, "", 50,-15.,  15., 50, 0., 100.));
        DDDetatheta.append(TH2D("3D_eta_theta_"+PDF[i]  , "", 50,-10.,  10., 45, 0., 180.));
        DDDetacost.append(TH2D("3D_eta_cost_"+PDF[i]    , "", 50,-15.,  15., 50,-1.,   1.));
	DDDmllcost.append(TH2D("3D_mll_cost_"+PDF[i]    , "", 50,  0., 300., 50,-1.,   1.));
	DDDth1th2.append(TH2D("3D_th1_th2_"+PDF[i]      , "", 45,  0., 180., 45, 0., 180.));
        DDpt1pt2.append(TH2D("2D_pt1_pt2_"+PDF[i]       , "", 50,  0.,  60., 50, 0.,  60.));
        DDphi1phi2.append(TH2D("2D_phi1_phi2_"+PDF[i]   , "", 45,  0., 180., 45, 0., 180.));
        DDptsumphi.append(TH2D("2D_ptsum_phi_"+PDF[i] 	, "", 50,  0., 120., 45, 0., 180.));
        DDpt1ptsum.append(TH2D("2D_pt1_ptsum_"+PDF[i] 	, "", 50,  0.,  60., 50, 0., 120.));
        DDpt2ptsum.append(TH2D("2D_pt2_ptsum_"+PDF[i] 	, "", 50,  0.,  60., 50, 0., 100.));
        DDmllptsum.append(TH2D("2D_mll_ptsum_"+PDF[i] 	, "", 50,  0., 140., 50, 0., 140.));
        DDetatheta.append(TH2D("2D_eta_theta_"+PDF[i]   , "", 50,-10.,  10., 45, 0., 180.));
        DDetacost.append(TH2D("2D_eta_cost_"+PDF[i]     , "", 50,-10.,  10., 50,-1.,   1.));
	DDmllcost.append(TH2D("2D_mll_cost_"+PDF[i]     , "", 50,  0., 180., 50,-1.,   1.));
        DDth1th2.append(TH2D("2D_th1_th2_"+PDF[i]       , "", 45,  0., 180., 45, 0., 180.));

	# LOOP OVER LINES IN LHE SAMPLE:

	# RESET EVENT COUNTING:
        event  = 0;
        evPASS = 0;
	# START LOOP:
        if (i == 5):
        	for j in xrange(337): # skip first 337 lines to avoid MG5 comments
                	f.next();
	else:
                for j in xrange(501): # skip first 500 lines to avoid MG5 comments
                        f.next();
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
                        if event%evtsplit==0: print "Event %i [%.2f%%]" % (event,perct);
                        elif event>Nevt: break;
		# 4-VECTORS FOR DECAY PRODUCTS:
		elif coll[0] == ' 13' or coll[0] == '-13' or coll[0] == ' 5' or coll[0] == '-5':
			dp = TLorentzVector();
			dm = TLorentzVector();
			px = float(coll[6]);
			py = float(coll[7]);
			pz = float(coll[8]);
			en = float(coll[9]);
			if coll[0] == ' 13' or ' 5': dp.SetXYZM(px,py,pz,en);
			if coll[0] == '-13' or '-5': dm.SetXYZM(px,py,pz,en);
		# CLOSE EVENT AND FILL HISTOGRAMS:
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
                            and dm.Pt() <= PTCUTUPPER
			):
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
                        elif ( cuts and not INNER
                            and (dp+dm).M() >= INVMCUTLOWER
                            and (dp+dm).M() <= INVMCUTUPPER
                            and (dp+dm).Pt() >= PTPAIRCUTLOWER
                            and (dp+dm).Pt() <= PTPAIRCUTUPPER
                            and abs((dp+dm).Eta()) >= ETAPAIRCUT
                            and dp.Pt() >= PTCUTLOWER
                            and dm.Pt() >= PTCUTLOWER
                            and dp.Pt() <= PTCUTUPPER
                            and dm.Pt() <= PTCUTUPPER
                        ):
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
	# End of loop over lines
        if cuts: print "Events passing acceptance: %i/%i" % (evPASS,event);
#        print "Integral of %s: %.6f nb" % (PDF[i],evPASS*xsec[i]/event);
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
plotlabel.AddText("MadGraphv5 #bullet #sqrt{s}=13 TeV #bullet "+EVTINPUT+" evt");

# Legend:
leg = TLegend(0.55,0.72,0.8,0.87);
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
for l in range(len(histoslog)):
	for m in range(len(FILES)):
                if scale:
                        histoslog[l][m].Scale(xsec[m]/Nevt*histoslog[l][m].GetBinWidth(1));
		histoslog[l][m].SetLineColor(m+2);
		histoslog[l][m].SetLineWidth(3);
		histoslog[l][m].SetLineStyle(m+1);
		globals()["hs_histoslog"+str(l)].Add(histoslog[l][m]);
                leg.AddEntry(histoslog[l][m]," "+PDF[m],"f");
	globals()["hs_histoslog"+str(l)].Draw("nostack hist");
	plotlabel.Draw("SAME");
	leg.Draw("SAME");
        if (scale):
                globals()["hs_histoslog"+str(l)].GetYaxis().SetTitle("d#sigma/d"+str(histoslog_axis[l])+str(histoslog_varx[l]));
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
	for k in range(len(FILE_TYPES)):
		canvas.Print(FILE_TYPES[k]+"/"+JOB+"_"+EVTINPUT+"evt_"+histoslog_label[l]+"."+FILE_TYPES[k]);
	leg.Clear();
# END loop over plots in log scale

# 2: 2D plot in log-scale:
canvas.SetLeftMargin(0.15);
canvas.SetBottomMargin(0.11);
canvas.SetRightMargin(0.23);
canvas.SetFrameFillColor(887);
gPad.SetLogy(0);
for l in range(len(DDlog)):
        for m in range(len(FILES)):
                if m==0:
                        continue;
                else:
			if (scale):
                        	DDlog[l][m].Scale(xsec[m]/Nevt*DDlog[l][m].GetXaxis().GetBinWidth(1));
                        DDlog[l][m].Draw("COLZ");
                        leg.AddEntry(DDlog[l][m]," "+PDF[m],"f");
        plotlabel.Draw("SAME");
        if (DDlog_label[l]=="DDptsumphi"):
                gPad.SetPhi(-30);
        elif (DDlog_label[l]=="DDmllptsum"):
                gPad.SetPhi(-120);
        else:
                gPad.SetPhi(210);
        DDlog[l][m].GetXaxis().SetTitleOffset(1.);
        DDlog[l][m].GetYaxis().SetTitleOffset(1.2);
        DDlog[l][m].GetZaxis().SetTitleOffset(1.55);
        DDlog[l][m].GetXaxis().SetTitleFont(42);
        DDlog[l][m].GetYaxis().SetTitleFont(42);
        DDlog[l][m].GetXaxis().SetLabelFont(42);
        DDlog[l][m].GetYaxis().SetLabelFont(42);
        DDlog[l][m].GetXaxis().SetTitleSize(0.05);
        DDlog[l][m].GetYaxis().SetTitleSize(0.05);
        DDlog[l][m].GetZaxis().SetTitleSize(0.05);
        DDlog[l][m].GetXaxis().SetLabelSize(0.04);
        DDlog[l][m].GetYaxis().SetLabelSize(0.04);
        DDlog[l][m].GetZaxis().SetLabelSize(0.04);
        if (scale):
	        DDlog[l][m].GetZaxis().SetTitle("d#sigma/d"+str(legoslog_xaxis[l])+"d"+str(legoslog_yaxis[l])+str(legoslog_varz[l]));
	else:
        	DDlog[l][m].GetZaxis().SetTitle("Events");
        DDlog[l][m].GetYaxis().SetTitle(DDlog_yaxis[l]+" "+DDlog_vary[l]+"");
        DDlog[l][m].GetXaxis().SetTitle(DDlog_xaxis[l]+" "+DDlog_varx[l]+"");
        DDlog[l][m].GetXaxis().SetDecimals(True);
        for k in range(len(FILE_TYPES)):
                canvas.Print(FILE_TYPES[k]+"/"+JOB+"_"+EVTINPUT+"evt_"+DDlog_label[l]+"."+FILE_TYPES[k]);
        leg.Clear();
# END loop over DDD Lego plots in log scale --

# 3: 3D LEGO plot in log-scale:
canvas.SetLeftMargin(0.15);
canvas.SetBottomMargin(0.11);
canvas.SetRightMargin(0.2);
canvas.SetFrameFillColor(0);
for l in range(len(legoslog)):
        for m in range(len(FILES)):
                if m==0:
                        continue;
                else:
			if (scale):
	                        legoslog[l][m].Scale(xsec[m]/Nevt*legoslog[l][m].GetXaxis().GetBinWidth(1));
                        legoslog[l][m].Draw("LEGO2Z");
                        leg.AddEntry(legoslog[l][m]," "+PDF[m],"f");
        plotlabel.Draw("SAME");
        if (legoslog_label[l]=="3Dptsumphi"):   gPad.SetPhi(-30);
        elif (legoslog_label[l]=="3Dmllptsum" or legoslog_label[l]=="3Dpt2ptsum"): gPad.SetPhi(-120);
        else: gPad.SetPhi(210);
        legoslog[l][m].GetXaxis().SetTitleOffset(1.30);
        legoslog[l][m].GetYaxis().SetTitleOffset(1.75);
        legoslog[l][m].GetZaxis().SetTitleOffset(1.40);
        legoslog[l][m].GetXaxis().SetTitleFont(42);
        legoslog[l][m].GetYaxis().SetTitleFont(42);
        legoslog[l][m].GetZaxis().SetTitleFont(42);
        legoslog[l][m].GetXaxis().SetTitleSize(0.05);
        legoslog[l][m].GetYaxis().SetTitleSize(0.05);
        legoslog[l][m].GetZaxis().SetTitleSize(0.05);
        legoslog[l][m].GetXaxis().SetLabelFont(42);
        legoslog[l][m].GetYaxis().SetLabelFont(42);
        legoslog[l][m].GetZaxis().SetLabelFont(42);
        legoslog[l][m].GetXaxis().SetLabelSize(0.03);
        legoslog[l][m].GetYaxis().SetLabelSize(0.03);
        legoslog[l][m].GetZaxis().SetLabelSize(0.03);
	if (scale):
	        legoslog[l][m].GetZaxis().SetTitle("d#sigma/d"+str(legoslog_xaxis[l])+"d"+str(legoslog_yaxis[l])+str(legoslog_varz[l]));
	else:
        	legoslog[l][m].GetZaxis().SetTitle("Events");
        legoslog[l][m].GetYaxis().SetTitle(legoslog_yaxis[l]+" "+legoslog_vary[l]+"");
        legoslog[l][m].GetXaxis().SetTitle(legoslog_xaxis[l]+" "+legoslog_varx[l]+"");
        legoslog[l][m].GetXaxis().SetDecimals(True);
        legoslog[l][m].Draw("LEGO2Z");
        plotlabel.Draw("SAME");
	canvas.Update();
	palette = legoslog[l][m].GetListOfFunctions().FindObject("palette");
	palette.SetX1NDC(0.81);
	palette.SetX2NDC(0.86);
	palette.SetY1NDC(0.24);
	palette.SetY2NDC(0.68);
	canvas.Modified();
	canvas.Update();
        for k in range(len(FILE_TYPES)):
                canvas.Print(FILE_TYPES[k]+"/"+JOB+"_"+EVTINPUT+"evt_"+legoslog_label[l]+"."+FILE_TYPES[k]);
        leg.Clear();
# END loop over DDD Lego plots in log scale --

FILEROOT.Write();

#####################################################################
#
# C'ESTI FINI
#
#####################################################################


