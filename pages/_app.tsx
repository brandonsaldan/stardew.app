import "../styles/globals.css";
import type { AppProps } from "next/app";
import { AnimatePresence, motion } from "framer-motion";
import { KVProvider } from "../contexts/KVContext";

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <main>
      <AnimatePresence>
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
        >
          <KVProvider>
            <Component {...pageProps} />
          </KVProvider>
        </motion.div>
      </AnimatePresence>
    </main>
  );
}

export default MyApp;
