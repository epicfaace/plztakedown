import * as anchor from '@project-serum/anchor';
import { Program } from '@project-serum/anchor';
import { Plztakedown } from '../target/types/plztakedown';

describe('plztakedown', () => {

  // Configure the client to use the local cluster.
  anchor.setProvider(anchor.Provider.env());

  const program = anchor.workspace.Plztakedown as Program<Plztakedown>;

  it('Is initialized!', async () => {
    // Add your test here.
    const tx = await program.rpc.initialize({});
    console.log("Your transaction signature", tx);
  });
});
