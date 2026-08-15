import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"
import { ImageLoaderProps } from "next/image"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function customImageLoader({src, width, quality} : ImageLoaderProps) {
  const isServer = typeof window === 'undefined';

  const baseUrl = isServer
  ? (process.env.INTERNAL_IMAGE_SERVER_URL || 'http://image-server:80')
  : (process.env.NEXT_PUBLIC_IMAGE_SERVER_URL || 'http://localhost:8080');

  const cleanSrc = src.startsWith("/") ? src : `/${src}`;

  return `${baseUrl}${cleanSrc}?w=${width}&q=${quality || 75}`;
}
