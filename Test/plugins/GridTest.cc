#include "TEST/Test/plugins/GridTest.h"

#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenLumiInfoHeader.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/LHERunInfoProduct.h"

using std::cout;
using std::endl;
using std::vector;

GridTest::GridTest(edm::ParameterSet const& cfg):
  mCands(mayConsume<pat::PackedCandidateCollection>(edm::InputTag("packedPFCandidates")))
{
  mTree = fs->make<TTree>("ProcessedTree","ProcessedTree");
  mTree->Branch("Pt", &mPt, "Pt/F");
  mTree->Branch("Eta", &mEta, "Eta/F");
  mTree->Branch("Phi", &mPhi, "Phi/F");
  mTree->Branch("E", &mE, "E/F");
  mTree->Branch("Ef_ECALRaw", &mEfEr, "Ef_ECALRaw/F");
  mTree->Branch("Ef_ECAL", &mEfE, "Ef_ECAL/F");
  mTree->Branch("Ef_HCALRaw", &mEfHr, "Ef_HCALRaw/F");
  mTree->Branch("Ef_HCAL", &mEfH, "Ef_HCAL/F");
}
//////////////////////////////////////////////////////////////////////////////////////////
void GridTest::beginJob() {}
//////////////////////////////////////////////////////////////////////////////////////////
void GridTest::endJob() {}
//////////////////////////////////////////////////////////////////////////////////////////
void GridTest::beginRun(edm::Run const & iRun, edm::EventSetup const& iSetup) {}
//////////////////////////////////////////////////////////////////////////////////////////
void GridTest::analyze(edm::Event const& event, edm::EventSetup const& iSetup) {
  edm::Handle<pat::PackedCandidateCollection> cands;
  event.getByToken(mCands, cands);

  // Pick the PF candidates removed by CHS (fromPV==0)
  int count = 0;
  for (auto cidx = 0u; cidx<cands->size(); ++cidx) {
    const auto &c = cands->at(cidx);
    if (c.pt()<5) continue;
    if (c.isPhoton() or c.isElectron() or c.isMuon()) continue;
    if (!c.isIsolatedChargedHadron()) continue;
    if (++count > 10) break;

    double calob = c.rawCaloFraction();
    double caloa = c.caloFraction();
    double hb = c.rawHcalFraction()*calob;
    double ha = c.hcalFraction()*caloa;
    double eb = calob-hb;
    double ea = caloa-ha;
    //hb *= c.energy();
    //ha *= c.energy();
    //ea *= c.energy();
    //eb *= c.energy();
    //cout << c.pt() << " " << c.pdgId() << " " << eb << "/" << ea << " " << hb << "/" << ha << endl;
    mPt  = c.pt();
    mEta = c.eta();
    mPhi = c.phi();
    mE   = c.energy();
    mEfEr = eb;
    mEfE  = ea;
    mEfHr = hb;
    mEfH  = ha;

    mTree->Fill();
  }
}

void GridTest::beginLuminosityBlock(edm::LuminosityBlock const& iLumi, edm::EventSetup const& set) {}


//////////////////////////////////////////////////////////////////////////////////////////
DEFINE_FWK_MODULE(GridTest);
