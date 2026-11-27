import type { Provider } from "@sponsorkit/shared";
import type { Env } from "../env";
import { githubAdapter } from "./github";
import { openCollectiveAdapter } from "./open-collective";
import type { ProviderAdapter } from "./types";

export function getAdapter(env: Env, provider: Provider): ProviderAdapter {
  return provider === "github" ? githubAdapter(env) : openCollectiveAdapter(env);
}

export * from "./types";
